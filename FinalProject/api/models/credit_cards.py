from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

#py -m uvicorn FinalProject.api.main:app --reload
#cd C:/Users/andmu/PycharmProjects/PG-21

class CreditCard(Base):
    __tablename__ = "credit_cards"

    #credit_cards table is supposed to be a subclass of payments table,
    #which is why they share the same primary key
    payment_id = Column(Integer, ForeignKey("payments.id"))
    card_num = Column(String(50))
    cvc = Column(String(5))

    __table_args__ = (
        PrimaryKeyConstraint("payment_id"),
        {},
    )
