from pydantic import BaseModel, Field
from typing import Optional

from FinalProject.api.models.customers import Customer


class ReviewBase(BaseModel):
    description: Optional[str] = Field(None, max_length=1000)
    score: Optional[float]


class ReviewCreate(ReviewBase):
    customer_id: int


class ReviewUpdate(BaseModel):
    description: Optional[str] = None
    score: Optional[float] = None
    customer_id: Optional[int] = None


class Review(ReviewBase):
    id: int
    customer: Customer
    class ConfigDict:
        from_attributes = True

