import os
import time
from celery import Celery

BROKER_URI = os.environ.get('BROKER_URI')
BACKEND_URI = os.environ.get('BACKEND_URI')

celery = Celery(
    'celery_app',
    broker=BROKER_URI,
    backend=BACKEND_URI,
    include=['app.tasks.predict_task', "app.tasks.train_task", 'app.tasks.validate_task']
)