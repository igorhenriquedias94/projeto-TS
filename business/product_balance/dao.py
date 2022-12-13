from sqlalchemy import Boolean, Column, ForeignKey, Integer
from ..database.database import Base

class ProductBalanceDAO(Base):
    __tablename__ = "product_balances"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    balance = Column(Integer, index=True)