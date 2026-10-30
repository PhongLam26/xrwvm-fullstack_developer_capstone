FROM node:22-bookworm-slim AS frontend
WORKDIR /frontend
COPY server/frontend/package*.json ./
RUN npm ci
COPY server/frontend/ ./
RUN npm run build

FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8000
WORKDIR /app
COPY server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY server/ ./
COPY --from=frontend /frontend/build ./frontend/build
RUN python manage.py collectstatic --noinput && mkdir -p /data
ENV DJANGO_DB_NAME=/data/db.sqlite3
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn djangoproj.wsgi:application --bind 0.0.0.0:${PORT} --workers 1 --threads 4 --timeout 90 --access-logfile -"]
