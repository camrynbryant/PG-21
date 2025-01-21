from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from ..schemas.orders import OrderNum

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/customer", response_model=list[schema.Order])
def read_all_customer(customer_id: int, db: Session = Depends(get_db)):
    """Returns all orders made by the customer"""
    return controller.read_all_customer(customer_id, db)

@router.get("/chef", response_model=list[schema.Order])
def read_all_chef(db: Session = Depends(get_db)):
    """Chef view of all orders data, which displays all food that is currently being prepared."""
    return controller.read_preparing_orders(db)

@router.get("/staff", response_model=list[schema.Order])
def read_all_staff(db: Session = Depends(get_db)):
    """Staff view of all orders data, which displays all orders."""
    return controller.read_all(db)

@router.get("/num-orders", response_model=schema.OrderNum)
def read_num_all(db: Session = Depends(get_db)):
    """Returns data on the total number of orders ever made"""
    return OrderNum(num_orders = controller.read_num_orders(db))

@router.get("/num-delivered-orders", response_model=schema.OrderNum)
def read_num_delivered(db: Session = Depends(get_db)):
    """Returns data on the total number of orders that have a status of \"Delivered\""""
    return OrderNum(num_orders = controller.read_num_delivered_orders(db))

@router.get("/num-preparing-orders", response_model=schema.OrderNum)
def read_num_preparing(db: Session = Depends(get_db)):
    """Returns data on the total number of orders that have a status of \"Preparing order\""""
    return OrderNum(num_orders = controller.read_num_preparing_orders(db))

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
