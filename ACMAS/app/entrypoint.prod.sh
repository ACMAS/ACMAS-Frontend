#!/bin/sh

# This file is used to verify that Postgres is healthy before applying migrations and running Gunicorn deployment
# PRODUCTION only -- Doesn't flush the db
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"