#! /bin/bash

cd /app

source /app/env/bin/activate

export DJANGO_SETTINGS_MODULE=app.settings

export SECRET_KEY=secret

export DEBUG=True


python manage.py migrate

python manage.py collectstatic --noinput

gunicorn app.wsgi:application --bind

exec "$@"

