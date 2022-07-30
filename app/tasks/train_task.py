import importlib
import logging
from celery import Task
from datetime import datetime
from app.config.celery_conifg import celery as app
from app.buysmart.linear_regression import volume_forecaster
from app.config.database import SessionLocal

@app.task(ignore_result=False,
          bind=True,
          name='{}.{}'.format(__name__, 'volume_forecaster'))
def train_and_predict_single_tank(tank_id):
    """
    Essentially the run method of PredictTask
    """
    with SessionLocal.begin() as db:
        volume_forecaster(db, tank_id, datetime.utcnow())
