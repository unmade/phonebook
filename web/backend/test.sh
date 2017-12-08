#!/usr/bin/env sh
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
cd .. && make test