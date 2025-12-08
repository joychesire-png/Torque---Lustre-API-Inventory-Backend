from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from models import get_db, Car, Catalogue,Order, Base, engine 


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500", "http://127.0.0.1:8000",  "http://localhost:3000", 
    "http://localhost:3001",       
    "http://localhost:5173",      
    "http://127.0.0.1:3000",     
    "http://127.0.0.1:3001",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Schemas
class CatalogueBase(BaseModel):
    name: str
    description: Optional[str] = None

class CatalogueCreate(CatalogueBase):
    pass

class CatalogueResponse(CatalogueBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float
    mileage: Optional[float] = None
    color: Optional[str] = None
    category_id: Optional[int] = None

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    product_id: int
    quantity: int = 1
    total_price: Optional[float] = None

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    description: Optional[str] = None

    
    class Config:
        from_attributes = True

   
#API Endpoints

@app.get("/")
def root():
    return {"message": "Torque & Lustre API", "status": "running"}

# Catalogue endpoints
@app.get("/catalogues", response_model=List[CatalogueResponse])
def get_catalogues(db: Session = Depends(get_db)):
    return db.query(Catalogue).all()

@app.post("/catalogues", response_model=CatalogueResponse)
def create_catalogue(catalogue: CatalogueCreate, db: Session = Depends(get_db)):
    db_catalogue = Catalogue(**catalogue.dict())
    db.add(db_catalogue)
    db.commit()
    db.refresh(db_catalogue)
    return db_catalogue

# Car endpoints
@app.get("/cars", response_model=List[CarResponse])
def get_cars(db: Session = Depends(get_db)):
    return db.query(Car).all()

@app.post("/cars", response_model=CarResponse)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# Order endpoints
@app.get("/orders", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@app.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order