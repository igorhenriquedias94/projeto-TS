from sqlalchemy import Boolean, Column, Integer, String
from ..database.database import Base

class UserDAO(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)