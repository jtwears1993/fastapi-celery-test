from tables import Col
from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime, PickleType
from sqlalchemy.orm import relationship

class TrainedModels(Base):

    __tablename__ = "ml_web_app_poc_trained_models"

    id = Column(Integer, primary_key=True, index=True)
    tank_id = Column(Integer, index=True)
    reporting_day = Column(DateTime)
    trained_model = Column(PickleType)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)