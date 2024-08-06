from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    review_text: Optional[str] = None
    rating: int

class ReviewCreate(ReviewBase):
    order_id: int
    customer_id: int

class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    rating: Optional[int] = None

class Review(ReviewBase):
    id: int
    order_id: int
    customer_id: int

    class Config:
        orm_mode = True
