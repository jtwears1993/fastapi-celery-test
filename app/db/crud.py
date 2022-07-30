from sqlalchemy.orm import Session
from app.db.daily_blocks import DailyBlocks
from app.db.predictions import Predictions
from app.db.trained_models import TrainedModels
from app.db.tanks import Tanks
import pandas as pd


# Create Opertations
def save_predictions(db: Session, tank_id, reporting_day):
    db_item = Predictions()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Read Operations
def get_volumes(db: Session, tank_id):
    return db.query(DailyBlocks).filter_by(tank_id=tank_id).order_by(DailyBlocks.reporting_day.asc()).all()

def get_enabled_tanks(db: Session):
    return db.query(Tanks.id).all()

def get_predictions_db(db: Session, tank_id):
    return db.query(Predictions).filter_by(tank_id=tank_id).order_by(Predictions.created_at.desc()).first()

def get_accuracy(db: Session, tank_id):
    return db.query(TrainedModels.trained_model).filter_by(tank_id=tank_id).order_by(TrainedModels.created_at.desc()).first()

# Delete Operations
def delete_predictions_db(db: Session, tank_id, reporting_day):
    pass

