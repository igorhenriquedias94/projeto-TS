from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from ..database.database import Base

class ItemDAO(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)