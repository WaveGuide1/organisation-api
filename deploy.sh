#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT --workers 3