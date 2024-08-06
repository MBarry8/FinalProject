from sqlalchemy import Column, Integer, String, DateTime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    promo_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    expiration_date = Column(DateTime, nullable=False)
