
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, DATETIME


class PromotionBase(BaseModel):
    code: Optional[str] = Field(None, max_length=50)
    discount_amt: Optional[float]
    expiration_date: Optional[datetime]


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount_amt: Optional[float] = None
    expiration_date: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
