#from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base #latest version

Base = declarative_base()

class Car (Base):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    mileage = Column(Float)
    color = Column(String)
    created_at = Column(DateTime, default = datetime.now)