#!/usr/bin/env sh

python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
/usr/bin/gunicorn phonebook.wsgi:application -w 2 -b :8000 --reload
