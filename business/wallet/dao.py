from sqlalchemy import Column, Integer, ForeignKey
from ..database.database import Base

class WalletDAO(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Integer, index=True)