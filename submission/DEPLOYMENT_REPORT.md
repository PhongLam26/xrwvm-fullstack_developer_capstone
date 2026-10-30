# IBM Code Engine deployment

Public URL: https://cars-web.2gkdcb8j96ze.us-south.codeengine.appdomain.cloud
Project: Code Engine - sn-labs-phonglam2599. Region: us-south. Project provided by Skills Network at no charge.

Three real Code Engine applications: cars-web (Django/Gunicorn/React/WhiteNoise), cars-api (Express/MongoDB), cars-sentiment (Flask/VADER). Built from public GitHub source commit bb49408. DEBUG=False; secret key generated inside the lab and stored in Code Engine secret cars-config. Host and CSRF origins restricted to the application URL; HTTPS cookies enabled.

Verified: public homepage, 50 dealers, static assets, registration, session login, GET logout with CSRF, dealer 8 details, review POST 201, independent GET and browser reload. See evidence/text/cloud_verification.json and four deployed screenshots. The review was submitted through the authenticated HTTPS API, then viewed and reloaded in Chrome.

Limitations: SQLite and MongoDB currently use container-local storage. They persist across HTTP requests/reloads but can be lost when Code Engine replaces the container. min-scale=1 and max-scale=1 reduce scale-to-zero events but do not provide durable storage. Persistent external databases are still required for a production deployment. Lab resources/URL can expire. This is a verified educational deployment, not a claim of production durability.
