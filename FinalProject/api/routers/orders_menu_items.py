from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders_menu_items as controller
from ..schemas import orders_menu_items as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['OrderMenuItems'],
    prefix="/orders-menu-items"
)


@router.post("/", response_model=schema.OrderMenuItem)
def create(request: schema.OrderMenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderMenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{order_tracking_num}/{menu_item_id}", response_model=schema.OrderMenuItem)
def read_one(order_tracking_num: int, menu_item_id: int, db: Session = Depends(get_db)):
    item_ids = [order_tracking_num, menu_item_id]
    return controller.read_one(db, item_ids = item_ids)


@router.put("/{order_tracking_num}/{menu_item_id}", response_model=schema.OrderMenuItem)
def update(order_tracking_num: int, menu_item_id: int,
           request: schema.OrderMenuItemUpdate, db: Session = Depends(get_db)):
    item_ids = [order_tracking_num, menu_item_id]
    return controller.update(db=db, request=request, item_ids=item_ids)


@router.delete("/{order_tracking_num}/{menu_item_id}")
def delete(order_tracking_num: int, menu_item_id: int, db: Session = Depends(get_db)):
    item_ids = [order_tracking_num, menu_item_id]
    return controller.delete(db=db, item_ids=item_ids)
