import numpy as np
import pandas as pd
from app.db.crud import get_predictions, get_volumes
from sqlalchemy.orm import Session


def _load_actuals(db: Session, tank_id: int) -> pd.Series:
    actuals = get_volumes(db, tank_id)
    actuals_df = pd.DataFrame.from_records(actuals)
    return actuals_df.total_volume

def _load_preds(db: Session, tank_id: int) -> pd.Series:
    preds = get_predictions(db, tank_id)
    preds_df = pd.DataFrame.from_records(preds)
    return preds_df.predicted_volume

def _mape(y_true: pd.Series, y_hat: pd.Series) -> float:
    n = y_true.shape[0]
    return (1/n) * np.nansum(abs(y_hat - y_true) / y_true)

def validate(db: Session, tank_id: int) -> float:
    actuals = _load_actuals(db, tank_id)
    preds = _load_preds(db, tank_id)
    return _mape(actuals, preds)