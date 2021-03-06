#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Exchange, Queue


""" Log config """
LOG_CONF_PATH         = 'conf/logger.conf'
LOG_ONLINE_FILE_PATH  = 'logs/online.log'
LOG_OFFLINE_FILE_PATH = 'logs/offline.log'
LOG_CELERY_FILE_PATH  = 'logs/celery.tasks.log'


""" Redis settings """
REDIS_HOST_DEFAULT = '127.0.0.1'
REDIS_PORT_DEFAULT = 6379
REDIS_DB_DEFAULT   = 0
REDIS_EXPIRE_DEFAULT =  3600 * 24 * 7


""" Key patterns """
PTN_HOT_IP = ''


""" Celery settings """
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_IMPORTS = ["tasks"]

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('email', Exchange('email'), routing_key='email'),
)

CELERY_ANNOTATIONS = {
    'tasks.send_email': {'rate_limit': '100/m'},
}
CELERY_ROUTES = {
    'tasks.send_email': {'queue': 'email'},
}


""" Send email task settings """
EMAIL_MAX_RETRIES = 2
EMAIL_DEFAULT_RETRY_DELAY = 60 * 3
EMAIL_SOFT_TIME_LIMIT = 10

""" Random background images """
RANDOM_BACKGROUND_IMAGES = 'img/share/background/random*.png'
