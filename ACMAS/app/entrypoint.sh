#!/bin/sh

# This file is used to verify that Postgres is healthy before applying migrations and running Gunicorn deployment
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# PRODUCTION only -- Doesn't flush the db
# Build the database based on models.py
python manage.py makemigrations ACMAS_Web
python manage.py migrate
python manage.py collectstatic --noinput

#Create a superuser
python manage.py ensure_admin --username="$DJANGO_USER" \
    --email="$DJANGO_EMAIL" \
    --password="$DJANGO_PASS"

python manage.py create_groups

exec "$@"