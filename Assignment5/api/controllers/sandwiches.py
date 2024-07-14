from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response

from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    update_data = sandwich.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_sandwich, key, value)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    db.delete(db_sandwich)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
