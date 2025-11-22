#!/bin/bash
set -e

echo "Waiting for database to be ready..."
sleep 2

echo "Running database migrations..."
alembic upgrade head 

echo "Checking if database needs seeding..."
python scripts/seed.py

echo "Starting Gunicorn..."
exec gunicorn -w ${API_WORKERS:-2} ${API_RELOAD:-} -b 0.0.0.0:8000 --log-level ${API_LOG_LEVEL:-info} wsgi:app