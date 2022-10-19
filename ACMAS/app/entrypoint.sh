#!/bin/sh
# This file is used to verify that Postgres is healthy before applying migrations and running Django dev server
# DEVELOPMENT only

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"