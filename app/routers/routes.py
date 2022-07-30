from fastapi import APIRouter
from starlette.responses import JSONResponse
from celery.result import AsyncResult
from datetime import datetime
from app.tasks.train_task import train_and_predict_single_tank
from app.tasks.validate_task import validate_single_tank
from app.db.crud import get_predictions_db, get_accuracy, delete_predictions_db
from app.config.database import SessionLocal

router = APIRouter(prefix='/buysmart', tags=['buysmart'], responses={404: {"description": "Not found"}})

@router.post("/buysmart/train-and-predict-model/{tank_id}", tags=["buysmart"], status_code=201)
def train_and_predict(tank_id) -> JSONResponse:
    task_id = train_and_predict_single_tank.delay(dict(tank_id))
    return {'task_id': str(task_id), 'status': 'Processing'}

@router.post("/buysmart/validate-model/{tank_id}", tags=["buysmart"], status_code=201)
def validate_model(tank_id) -> JSONResponse:
    task_id = validate_single_tank.delay(dict(tank_id))
    return {'task_id': str(task_id), 'status': 'Processing'}

@router.get("/buysmart/validation-results/{tank_id}", tags=["buysmart"], status_code=200)
def get_model_accruacy(tank_id) -> JSONResponse:
    with SessionLocal.begin() as db:
        model_accuracy = get_accuracy(db, tank_id)
    return {"accuracy": model_accuracy}

@router.get("/buysmart/get-predictions/{tank_id}", tags=["buysmart"], status_code=200)
def get_predictions(tank_id) -> JSONResponse:
    with SessionLocal.begin() as db:
        preds: list = get_predictions_db()
    return 200, {"tank_id": tank_id, "predictions": preds}

@router.post("/buysmart/delete-predictions/{tank_id}", tags=["buysmart"], status_code=201)
def delete_predictions(tank_id) -> JSONResponse:
    with SessionLocal.begin() as db:
        delete_predictions_db(db, tank_id, datetime.utcnow())


