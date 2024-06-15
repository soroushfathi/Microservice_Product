#!/bin/sh

echo "--> Waiting for db to be ready"
./wait-for-it.sh db:5432

# Apply database migrations
echo "Apply database migrations"
python ./ProductService/manage.py makemigrations
python ./ProductService/manage.py migrate
python ./ProductService/manage.py collectstatic --clear --noinput
python ./ProductService/manage.py collectstatic --noinput

# Start server
echo "--> Starting web process"
cd ProductService
gunicorn config.wsgi:application -b 0.0.0.0:8000
