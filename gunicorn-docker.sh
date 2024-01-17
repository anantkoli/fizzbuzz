#!/bin/bash

# RUN this file like : sudo sh gunicorn-docker.sh var fizzbuzz 0.0.0.0:8000

PROJ_DIR=/$1/www/$2
ACCESS_LOG_FILE=/var/log/fizzbuzz/gunicorn_access.log
ERROR_LOG_FILE=/var/log/fizzbuzz/gunicorn_error.log

cd $PROJ_DIR
mkdir /var/log/fizzbuzz
WORKERS=2

gunicorn -w $WORKERS fizzbuzz.wsgi:application --preload -b $3 -t 0 \
    --log-level ERROR \
    --max-requests 100 \
    --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(L)s"' \
    --access-logfile $ACCESS_LOG_FILE \
    --error-logfile $ERROR_LOG_FILE
    
