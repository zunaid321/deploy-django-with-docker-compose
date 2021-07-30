#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

pip install -r requirements.txt
python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module backend.wsgi
