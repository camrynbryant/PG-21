from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customers_payments_promotions as controller
from ..schemas import customers_payments_promotions as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['CustomersPaymentsPromotions'],
    prefix="/customers-payments-promotions"
)


@router.post("/", response_model=schema.CustomerPaymentPromotion)
def create(request: schema.CustomerPaymentPromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.CustomerPaymentPromotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{customer_id}/{payment_id}/{promotion_id}", response_model=schema.CustomerPaymentPromotion)
def read_one(customer_id: int, payment_id: int, promotion_id: int, db: Session = Depends(get_db)):
    item_ids = [customer_id, payment_id, promotion_id]
    return controller.read_one(db, item_ids=item_ids)


@router.put("/{customer_id}/{payment_id}/{promotion_id}", response_model=schema.CustomerPaymentPromotion)
def update(customer_id: int, payment_id: int, promotion_id: int,
           request: schema.CustomerPaymentPromotionUpdate, db: Session = Depends(get_db)):
    item_ids = [customer_id, payment_id, promotion_id]
    return controller.update(db=db, request=request, item_ids=item_ids)


@router.delete("/{customer_id}/{payment_id}/{promotion_id}")
def delete(customer_id: int, payment_id: int, promotion_id: int, db: Session = Depends(get_db)):
    item_ids = [customer_id, payment_id, promotion_id]
    return controller.delete(db=db, item_ids=item_ids)
