#!/usr/bin/env sh

cd phonebook
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
/usr/bin/gunicorn phonebook.wsgi:application -w 2 -b :8000 --reload
