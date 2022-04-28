#!/bin/sh

python3 manage.py gunicorn -b 0.0.0.0:5000
