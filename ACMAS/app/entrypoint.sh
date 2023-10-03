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

#Set up a superuser
echo "from django.contrib.auth.models import User; 
User.objects.create_superuser('$DJANGO_USER', '$DJANGO_EMAIL', '$DJANGO_PASS')" | python manage.py shell

exec "$@"