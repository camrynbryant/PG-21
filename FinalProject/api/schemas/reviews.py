from pydantic import BaseModel, Field
from typing import Optional


class ReviewBase(BaseModel):
    description: Optional[str] = Field(None, max_length=1000)
    score: Optional[float]


class ReviewCreate(ReviewBase):
    description: str
    score: float
    customer_id: int


class ReviewUpdate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True
