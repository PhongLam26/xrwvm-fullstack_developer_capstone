import json
import logging
from datetime import date

import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST

from . import restapis
from .models import CarMake, CarModel
from .populate import initiate

logger = logging.getLogger(__name__)


def frontend(request):
    try:
        return HttpResponse(render_to_string("index.html", request=request))
    except Exception:
        return HttpResponse(
            "The React frontend has not been built yet. Run npm run build in server/frontend.",
            status=503,
            content_type="text/plain",
        )


def _body_json(request):
    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def _service_error(error):
    logger.warning("Connected service request failed: %s", error)
    return JsonResponse(
        {"status": 502, "error": "A connected service is unavailable."},
        status=502,
    )


def _proxy_get(endpoint, key, not_found_message=None):
    try:
        result = restapis.get_request(endpoint)
    except requests.HTTPError as error:
        if error.response is not None and error.response.status_code == 404:
            return JsonResponse(
                {"status": 404, "error": not_found_message or "Not found."},
                status=404,
            )
        return _service_error(error)
    except (requests.RequestException, ValueError) as error:
        return _service_error(error)

    if not isinstance(result, list):
        return JsonResponse(
            {"status": 502, "error": "Connected service returned invalid data."},
            status=502,
        )
    if not result and not_found_message:
        return JsonResponse(
            {"status": 404, "error": not_found_message}, status=404
        )
    return JsonResponse({"status": 200, key: result})


@require_GET
@ensure_csrf_cookie
def csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})


@require_POST
def login_user(request):
    payload = _body_json(request)
    if payload is None:
        return JsonResponse({"status": 400, "error": "Expected a JSON object."}, status=400)

    username = str(payload.get("userName", payload.get("username", ""))).strip()
    password = str(payload.get("password", ""))
    if not username or not password:
        return JsonResponse(
            {"status": 400, "error": "Username and password are required."},
            status=400,
        )

    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse(
            {"status": 401, "error": "Invalid username or password."}, status=401
        )
    login(request, user)
    return JsonResponse(
        {
            "status": "Authenticated",
            "userName": user.username,
            "firstName": user.first_name,
            "lastName": user.last_name,
        }
    )


@require_POST
def logout_user(request):
    logout(request)
    return JsonResponse({"status": 200, "message": "Logged out."})


@require_POST
def register_user(request):
    payload = _body_json(request)
    if payload is None:
        return JsonResponse({"status": 400, "error": "Expected a JSON object."}, status=400)

    username = str(payload.get("username", "")).strip()
    first_name = str(payload.get("first_name", "")).strip()
    last_name = str(payload.get("last_name", "")).strip()
    email = str(payload.get("email", "")).strip()
    password = str(payload.get("password", ""))
    if not all((username, first_name, last_name, email, password)):
        return JsonResponse(
            {"status": 400, "error": "All five registration fields are required."},
            status=400,
        )
    if User.objects.filter(username__iexact=username).exists():
        return JsonResponse(
            {"status": 409, "error": "That username is already registered."},
            status=409,
        )
    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse(
            {"status": 409, "error": "That email address is already registered."},
            status=409,
        )
    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        return JsonResponse({"status": 400, "error": "Enter a valid email address."}, status=400)
    if len(password) < 8:
        return JsonResponse(
            {"status": 400, "error": "Password must contain at least 8 characters."},
            status=400,
        )

    user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    try:
        user.full_clean(exclude=("password",))
    except ValidationError as error:
        return JsonResponse({"status": 400, "error": error.messages}, status=400)
    user.set_password(password)
    user.save()
    return JsonResponse({"status": 201, "message": "Account created."}, status=201)


@require_GET
def get_dealerships(request):
    return _proxy_get("fetchDealers", "dealers")


@require_GET
def get_dealerships_by_state(request, state):
    if state.lower() == "all":
        return get_dealerships(request)
    return _proxy_get(f"fetchDealers/{state}", "dealers")


@require_GET
def get_dealer_details(request, dealer_id):
    return _proxy_get(
        f"fetchDealer/{dealer_id}", "dealer", f"Dealer {dealer_id} was not found."
    )


@require_GET
def get_dealer_reviews(request, dealer_id):
    try:
        reviews = restapis.get_request(f"fetchReviews/dealer/{dealer_id}")
        if not isinstance(reviews, list):
            raise ValueError("Review service returned invalid data.")
        for review in reviews:
            if not review.get("sentiment"):
                review["sentiment"] = restapis.analyze_review_sentiments(
                    review.get("review", "")
                )["sentiment"]
    except (requests.RequestException, ValueError) as error:
        return _service_error(error)
    return JsonResponse({"status": 200, "reviews": reviews})


@require_POST
def add_review(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": 401, "error": "Sign in to submit a review."}, status=401)

    payload = _body_json(request)
    if payload is None:
        return JsonResponse({"status": 400, "error": "Expected a JSON object."}, status=400)
    required = ("dealership", "review", "purchase_date", "car_make", "car_model", "car_year")
    if any(not str(payload.get(field, "")).strip() for field in required):
        return JsonResponse({"status": 400, "error": "All review fields are required."}, status=400)

    try:
        dealer_id = int(payload["dealership"])
        car_year = int(payload["car_year"])
        date.fromisoformat(str(payload["purchase_date"]))
    except (TypeError, ValueError):
        return JsonResponse({"status": 400, "error": "Dealer, date, or model year is invalid."}, status=400)
    if not 2015 <= car_year <= 2023:
        return JsonResponse({"status": 400, "error": "Car year must be from 2015 to 2023."}, status=400)

    try:
        dealer = restapis.get_request(f"fetchDealer/{dealer_id}")
        if not dealer:
            return JsonResponse({"status": 404, "error": "Dealer was not found."}, status=404)
        sentiment = restapis.analyze_review_sentiments(str(payload["review"]))["sentiment"]
        user = request.user
        display_name = " ".join(part for part in (user.first_name, user.last_name) if part)
        review = restapis.post_review(
            {
                "name": display_name or user.username,
                "dealership": dealer_id,
                "review": str(payload["review"]).strip(),
                "purchase": bool(payload.get("purchase", True)),
                "purchase_date": str(payload["purchase_date"]),
                "car_make": str(payload["car_make"]).strip(),
                "car_model": str(payload["car_model"]).strip(),
                "car_year": car_year,
                "sentiment": sentiment,
            }
        )
    except (requests.RequestException, ValueError) as error:
        return _service_error(error)
    return JsonResponse(
        {"status": 201, "review": review, "sentiment": sentiment}, status=201
    )


@require_GET
def get_cars(request):
    if not CarModel.objects.exists():
        initiate()
    models = CarModel.objects.select_related("car_make").all()
    car_models = [
        {
            "id": model.id,
            "CarMake": model.car_make.name,
            "CarModel": model.name,
            "type": model.type,
            "year": model.year,
        }
        for model in models
    ]
    return JsonResponse({"status": 200, "CarModels": car_models})


@require_GET
def get_carmakes(request):
    if not CarModel.objects.exists():
        initiate()
    makes = list(CarMake.objects.values("id", "name", "description"))
    models = list(
        CarModel.objects.select_related("car_make").values(
            "id", "name", "type", "year", "car_make__name"
        )
    )
    return JsonResponse({"status": 200, "CarMakes": makes, "CarModels": models})
