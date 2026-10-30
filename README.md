# xrwvm-fullstack_developer_capstone
## Cars Dealership — Full-stack Development Capstone

IBM starter implementation for browsing dealerships, registration, authentication, car catalogs and reviews.

## Architecture
React → Django session authentication/API proxy → Express → MongoDB.
Django stores users and car makes/models in SQLite. Flask uses the supplied NLTK VADER lexicon for sentiment.

## Structure
- server/djangoapp: authentication, proxy, models, migrations and tests
- server/database: Express and IBM seed data
- server/frontend: React and standalone About/Contact pages
- submission: evidence and reports
- .github/workflows: CI

## Windows setup
Create a virtual environment with python -m venv .venv, then install server/requirements.txt using its Python executable.
Run docker compose -p cars-capstone up -d --build at project root.
Run npm ci and npm run build in server/frontend.
Run manage.py migrate and manage.py runserver 127.0.0.1:8010 in server using the virtual environment.
Open http://127.0.0.1:8010/. Node uses 3030 and sentiment uses 5050.
Create an administrator with manage.py createsuperuser. Generated local credentials are excluded from Git.

## APIs
GET /djangoapp/csrf prepares CSRF. POST /djangoapp/register, /login and /logout use JSON and CSRF headers.
GET /djangoapp/get_dealers, /get_dealers/Kansas, /dealer/8, /reviews/dealer/8, /get_cars, /get_carmakes.
POST /djangoapp/add_review requires a session.
Node: /fetchDealers, /fetchDealers/Kansas, /fetchDealer/8, /fetchReviews/dealer/8, /insert_review.
Sentiment: GET http://127.0.0.1:5050/analyze/Fantastic%20services.

## Tests and CI
Run manage.py test using the virtual environment. Run npm run build in frontend.
GitHub Actions runs Django checks/tests, React build, Node syntax checks and container builds.

## Data
Original IBM synthetic data is retained. demo_reviews.json adds a documented Kansas demo review.
MongoDB uses a named volume; seed runs only on empty collections and preserves posted reviews.
SQLite is local and excluded from Git.

## Deployment
IBM Cloud deployment was omitted at the user's request. No public deployment URL is claimed. Q1–Q22 have verified evidence; Q23–Q27 remain incomplete. See submission/SUBMISSION_ANSWERS.md.
Production needs DJANGO_DEBUG=false, DJANGO_SECRET_KEY, DJANGO_ALLOWED_HOSTS, DJANGO_CSRF_TRUSTED_ORIGINS, BACKEND_URL, SENTIMENT_ANALYZER_URL, persistent databases and static-file serving configuration.

## Attribution
Based on ibm-developer-skills-network/xrwvm-fullstack_developer_capstone.
Original Apache 2.0 license and Git history retained.
