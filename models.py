from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship #latest version 

engine = create_engine('sqlite:///TorqueandLustre.db', echo=True)
SessionLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

Base = declarative_base()

class Catalogue (Base):
    __tablename__ = 'catalogues'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default = datetime.now)

    cars = relationship("Car", back_populates="catalogue")

class Car(Base):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True, index =True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    mileage = Column(Float)
    color = Column(String)
    category_id = Column(Integer, ForeignKey('catalogues.id'))
    created_at = Column(DateTime, default=datetime.now)
    
    catalogue = relationship("Catalogue", back_populates="cars")
    orders = relationship("Order", back_populates="car")
class Order (Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index =True)
    product_id = Column(Integer, ForeignKey('cars.id'))
    quantity = Column(Integer, default=1)
    total_price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    
    car = relationship("Car", back_populates="orders")

