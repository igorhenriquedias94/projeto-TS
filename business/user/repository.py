from sqlalchemy.orm import Session

from .dao import UserDAO
from .model import User, UserCreate


class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(UserDAO).filter(UserDAO.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(UserDAO).filter(UserDAO.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(UserDAO).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        db_user = UserDAO(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user: User):
        db_user = self.db.query(UserDAO).filter(UserDAO.id == user.id).first()
        db_user.email = user.email
        db_user.name = user.name
        db_user.is_active = user.is_active
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def delete_user(self, user_id: int):
        db_user = self.db.query(UserDAO).filter(UserDAO.id == user_id).first()
        self.db.delete(db_user)
        self.db.commit()
        return db_user