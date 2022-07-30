from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime
from sqlalchemy.orm import relationship

class Predictions(Base):

    __tablename__ = "ml_web_app_poc_predictions"

    id = Column(Integer, primary_key=True, index=True) 
    tank_id = Column(Integer, index=True)
    reporting_day = Column(DateTime)
    predicted_volume = Column(Float)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)