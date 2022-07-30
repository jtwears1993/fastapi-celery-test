from pydantic import BaseModel
from datetime import datetime

class Predictions(BaseModel):
    id: int
    tank_id: int
    reporting_day: datetime
    predicted_volume: float
    created_at: datetime
    updated_at: datetime
    

   