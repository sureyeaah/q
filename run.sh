#!/usr/bin/env bash

screen -dmS redis bash -c 'redis-server; exec sh'
screen -dmS flask bash -c 'export FLASK_APP=app.py; flask run >& server.log; exec sh'
screen -dmS celery_scheduler bash -c 'celery -A tasks worker --concurrency=1 --loglevel=INFO -Q scheduler -n scheduler_worker@%h -f scheduler.log; exec sh'
screen -dmS celery_worker bash -c 'celery -A tasks worker --concurrency=4 --loglevel=INFO -Q worker -n merge@%h -f tasks.log; exec sh'
