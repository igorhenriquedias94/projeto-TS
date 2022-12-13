from .repository import UserRepository, UserCreate, User
from ..wallet.service import WalletService
from sqlalchemy.orm import Session

class UserService():
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        self.wallet_service = WalletService(db)
        
    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)
    
    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)
    
    def get_users_page(self, skip: int, limit: int):
        return self.user_repository.get_users(skip, limit)
    
    def create_user_with_wallet(self, user: UserCreate):
        user = self.create_user(user)
        self.wallet_service.create_wallet(user.id)
        return user
    
    def create_user(self, user: UserCreate):
        return self.user_repository.create_user(user)
    
    def update_user(self, user: User):
        return self.user_repository.update_user(user)
    
    def delete_user(self, user_id: int):
        return self.user_repository.delete_user(user_id)
