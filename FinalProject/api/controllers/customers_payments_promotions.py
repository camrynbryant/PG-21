from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers_payments_promotions as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.CustomerPaymentPromotion(
        customer_id = request.customers,
        payment_id = request.payments,
        promotion_id = request.promotions
    )


def read_all(db: Session):
    try:
        result = db.query(model.CustomerPaymentPromotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_ids):
    """

    :param db:
    :param item_ids: an object that contains the 3 attributes which make up the primary key of the
    customers_payments_promotions table. These 3 attributes include customer_id, payment_id, and promotion_id.
    :return:
    """
    try:
        customer_id = item_ids.customer_id
        payment_id = item_ids.payment_id
        promotion_id = item_ids.promotion_id

        item = (db.query(model.CustomerPaymentPromotion).
                filter(model.CustomerPaymentPromotion.customer_id == customer_id,
                       model.CustomerPaymentPromotion.payment_id == payment_id,
                       model.CustomerPaymentPromotion.promotion_id == promotion_id).first())
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, item_ids, request):
    try:
        customer_id = item_ids.customer_id
        payment_id = item_ids.payment_id
        promotion_id = item_ids.promotion_id

        item = (db.query(model.CustomerPaymentPromotion)
                .filter(model.CustomerPaymentPromotion.customer_id == customer_id,
                       model.CustomerPaymentPromotion.payment_id == payment_id,
                       model.CustomerPaymentPromotion.promotion_id == promotion_id))
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Customer_id, Payment_id, or Promotion_id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_ids):
    try:
        customer_id = item_ids.customer_id
        payment_id = item_ids.payment_id
        promotion_id = item_ids.promotion_id

        item = (db.query(model.CustomerPaymentPromotion)
                .filter(model.CustomerPaymentPromotion.customer_id == customer_id,
                       model.CustomerPaymentPromotion.payment_id == payment_id,
                       model.CustomerPaymentPromotion.promotion_id == promotion_id))
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Customer_id, Payment_id, or Promotion_id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)






