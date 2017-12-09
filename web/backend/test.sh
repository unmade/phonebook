#!/usr/bin/env sh
cd .. && isort --check-only -q && pylint phonebook/* --errors-only && cd -
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
cd .. && make test