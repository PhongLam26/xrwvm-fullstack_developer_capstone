import json
import requests
from unittest.mock import patch
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .populate import initiate
from .models import CarMake, CarModel

class AuthenticationTests(TestCase):
    def test_admin_username_and_logout_protection(self):
        user = User.objects.create_superuser(
            'root', 'admin@example.com', 'Local-test-admin-238!', first_name='Demo'
        )
        self.client.force_login(user)
        response = self.client.get('/admin/')
        self.assertContains(response, '<strong>root</strong>', html=True)
        self.assertEqual(self.client.post('/admin/logout/').status_code, 200)
        self.assertRedirects(
            self.client.get('/admin/'), '/admin/login/?next=/admin/'
        )

    @patch('djangoapp.restapis.get_request')
    def test_missing_dealer_returns_404(self, get):
        get.return_value = []
        self.assertEqual(self.client.get('/djangoapp/dealer/999999').status_code, 404)

    @patch('djangoapp.restapis.get_request')
    def test_unavailable_backend_returns_502(self, get):
        get.side_effect = requests.ConnectionError('Service unavailable')
        self.assertEqual(self.client.get('/djangoapp/get_dealers').status_code, 502)

    def post(self,path,data):
        return self.client.post("/djangoapp/"+path,json.dumps(data),content_type="application/json")
    def test_registration_duplicate_and_password_hash(self):
        data=dict(username="reviewer",first_name="Demo",last_name="Driver",email="demo@example.com",password="Test-account-238!")
        self.assertEqual(self.post("register",data).status_code,201)
        user=User.objects.get(username="reviewer")
        self.assertNotEqual(user.password,data["password"])
        self.assertTrue(user.check_password(data["password"]))
        self.assertEqual(self.post("register",data).status_code,409)
    def test_login_failure_logout_and_revoked_session(self):
        User.objects.create_user("driver",password="Test-account-238!")
        self.assertEqual(self.post("login",dict(userName="driver",password="wrong")).status_code,401)
        self.assertEqual(self.post("login",dict(userName="driver",password="Test-account-238!")).status_code,200)
        self.assertIn("_auth_user_id",self.client.session)
        self.assertEqual(self.post("logout",{}).status_code,200)
        self.assertNotIn("_auth_user_id",self.client.session)
        self.assertEqual(self.post("add_review",{}).status_code,401)
    def test_csrf_enforced(self):
        client=Client(enforce_csrf_checks=True)
        self.assertEqual(client.post("/djangoapp/login","{}",content_type="application/json").status_code,403)
    def test_catalog_seed_idempotent(self):
        first=initiate(); second=initiate()
        self.assertEqual(first,second)
        self.assertGreater(CarMake.objects.count(),0)
        self.assertGreater(CarModel.objects.count(),0)
        self.assertEqual(self.client.get("/djangoapp/get_carmakes").status_code,200)
    @patch("djangoapp.restapis.get_request")
    def test_dealer_proxy_and_state(self,get):
        get.return_value=[dict(id=8,state="Kansas")]
        self.assertEqual(self.client.get("/djangoapp/get_dealers/Kansas").json()["dealers"][0]["state"],"Kansas")
        get.assert_called_with("fetchDealers/Kansas")
    @patch("djangoapp.restapis.post_review")
    @patch("djangoapp.restapis.analyze_review_sentiments")
    @patch("djangoapp.restapis.get_request")
    def test_authenticated_review_uses_session_name(self,get,sentiment,post):
        user=User.objects.create_user("driver",password="Test-account-238!",first_name="Demo",last_name="Driver")
        self.client.force_login(user)
        get.return_value=[dict(id=8)]
        sentiment.return_value={"sentiment":"positive"}
        post.return_value={"id":52}
        payload=dict(dealership=8,review="Fantastic services",purchase_date="2024-06-15",car_make="Toyota",car_model="Camry",car_year=2022)
        response=self.post("add_review",payload)
        self.assertEqual(response.status_code,201)
        self.assertEqual(post.call_args.args[0]["name"],"Demo Driver")
