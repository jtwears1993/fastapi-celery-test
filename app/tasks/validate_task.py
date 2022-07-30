import logging
from app.config.celery_conifg import celery as app
from app.config.database import SessionLocal
from app.buysmart.validate import validate

@app.task(ignore_result=False,
          bind=True,
          name='{}.{}'.format(__name__, 'validate-results'))
def validate_single_tank(tank_id):
    """
    Celery task which queues, executes 
    and returns asynchrounusly validations 
    of the volume forecasts
    """
    with SessionLocal.begin() as db:

        validate(db, tank_id)
