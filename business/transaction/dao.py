from sqlalchemy import Boolean, Column, ForeignKey, Integer
from ..database.database import Base

class TransactionDAO(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    buyer_id = Column(Integer, ForeignKey("users.id"))
    seller_id = Column(Integer, ForeignKey("users.id"))
    price = Column(Integer, index=True)
    balance = Column(Integer, index=True)