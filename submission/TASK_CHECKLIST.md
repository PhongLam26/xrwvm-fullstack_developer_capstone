# Task checklist

Updated after the graded 29/50 attempt. All 27 question slots now have real evidence; production persistence is still incomplete. No new grade is claimed.

|Task|Requirement|Status|Source|Evidence|Verification / notes|
|---|---|---|---|---|---|
|1|README|COMPLETE_VERIFIED|`README.md`|GitHub API contents verification|Public source URL in Q1|
|2|Django server|COMPLETE_VERIFIED|`server/manage.py`|evidence/text/django_server|HTTP 200 on :8010|
|3|About Us|COMPLETE_VERIFIED|`server/frontend/static/About.html`|GitHub API contents verification|Public source URL in Q3|
|4|Contact Us|COMPLETE_VERIFIED|`server/frontend/static/Contact.html`|GitHub API contents verification|Public source URL in Q4|
|5|Login|COMPLETE_VERIFIED|`server/djangoapp/views.py`|evidence/text/loginuser|Real CSRF/session request|
|6|Logout|COMPLETE_VERIFIED|`server/djangoapp/views.py`|evidence/text/logoutuser|Session invalidation test passes|
|7|Register|COMPLETE_VERIFIED|`server/frontend/src/components/Register/Register.jsx`|GitHub API contents verification|Five fields; registration/duplicate tests pass|
|8|Dealer reviews API|COMPLETE_VERIFIED|`server/database/app.js`|evidence/text/getdealerreviews|Real cURL; dealer 8 has reviews|
|9|All dealers API|COMPLETE_VERIFIED|`server/database/app.js`|evidence/text/getalldealers|Real cURL; 50 dealers|
|10|Dealer by ID|COMPLETE_VERIFIED|`server/database/app.js`|evidence/text/getdealerbyid|Real cURL; ID 8|
|11|Kansas dealers|COMPLETE_VERIFIED|`server/database/app.js`|evidence/text/getdealersbyState|Real cURL; Kansas|
|12|Admin login|COMPLETE_VERIFIED|`server/djangoapp/templates/admin/base_site.html`|evidence/screenshots/admin_login.png|Browser login with root; visible ROOT|
|13|Admin logout|COMPLETE_VERIFIED|`server/djangoproj/urls.py`|evidence/screenshots/admin_logout.png|Logged out; reopening admin redirects to login|
|14|Car makes|COMPLETE_VERIFIED|`server/djangoapp/models.py`|evidence/text/getallcarmakes|Seeded catalog API and relational test|
|15|Car models|COMPLETE_VERIFIED|`server/djangoapp/models.py`|evidence/text/getallcarmakes|Seeded catalog API and relational test|
|16|Sentiment analysis|COMPLETE_VERIFIED|`server/djangoapp/microservices/app.py`|evidence/text/analyzereview|Fantastic services classified positive by VADER|
|17|Guest home|COMPLETE_VERIFIED|`server/frontend/src/components/Dealers/Dealers.jsx`|evidence/screenshots/get_dealers.png|Real Chrome guest home|
|18|Logged-in home|COMPLETE_VERIFIED|`server/frontend/src/components/Dealers/Dealers.jsx`|evidence/screenshots/get_dealers_loggedin.png|Username, Review Dealer, address bar visible|
|19|State filter|COMPLETE_VERIFIED|`server/frontend/src/components/Dealers/Dealers.jsx`|evidence/screenshots/dealersbystate.png|Kansas selected; dealer 8; URL visible|
|20|Dealer detail|COMPLETE_VERIFIED|`server/frontend/src/components/Dealers/Dealer.jsx`|evidence/screenshots/dealer_id_reviews.png|Dealer 8 details and stored reviews|
|21|Filled review form|COMPLETE_VERIFIED|`server/frontend/src/components/Dealers/PostReview.jsx`|evidence/screenshots/dealership_review_submission.png|All fields filled before submit|
|22|Posted review|COMPLETE_VERIFIED|`server/frontend/src/components/Dealers/PostReview.jsx`|evidence/screenshots/added_review.png|Submitted in browser; review 52 verified via backend and reload|
|23|GitHub Actions|COMPLETE_VERIFIED|`.github/workflows/ci.yml`|evidence/text/CICD|Real successful GitHub Actions run; full log saved|
|24|Deployment URL|IMPLEMENTED_NOT_VERIFIED|Dockerfile / Code Engine|See DEPLOYMENT_REPORT.md and Q23|Live deployment verified; container replacement persistence incomplete|
|25|Deployed landing|COMPLETE_VERIFIED|Dockerfile / Code Engine|See DEPLOYMENT_REPORT.md and Q24|Live deployment verified; container replacement persistence incomplete|
|26|Deployed login|COMPLETE_VERIFIED|Dockerfile / Code Engine|See DEPLOYMENT_REPORT.md and Q25|Live deployment verified; container replacement persistence incomplete|
|27|Deployed detail|COMPLETE_VERIFIED|Dockerfile / Code Engine|See DEPLOYMENT_REPORT.md and Q26|Live deployment verified; container replacement persistence incomplete|
|28|Deployed review|COMPLETE_VERIFIED|Dockerfile / Code Engine|See DEPLOYMENT_REPORT.md and Q27|Live deployment verified; container replacement persistence incomplete|
