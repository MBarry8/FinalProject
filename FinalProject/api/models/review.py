from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    review_text = Column(String(500))
    rating = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="reviews")
    order = relationship("Order", back_populates="review")
