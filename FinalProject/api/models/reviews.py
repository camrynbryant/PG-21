from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(1000))
    score = Column(Double())
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customers = relationship("Customer", back_populates="reviews")