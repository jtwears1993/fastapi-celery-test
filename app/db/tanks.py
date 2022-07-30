from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime, Numeric
from sqlalchemy.orm import relationship

class Tanks(Base):

    __tablename__ = "tanks"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer)
    fuel_grade_id = Column(Integer)
    number = Column(Integer)
    max_volume = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    virtual_tank_id = Column(Integer)
    min_threshold = Column(Float)
    split_ratio =  Column(Float)
    deleted_at = Column(DateTime)
    scalar = Column(Numeric)
