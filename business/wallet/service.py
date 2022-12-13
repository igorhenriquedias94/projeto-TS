from .repository import WalletRepository, WalletCreate, Wallet
from sqlalchemy.orm import Session

class WalletService():
    def __init__(self, db: Session):
        self.wallet_repository = WalletRepository(db)
        
    def get_wallet_by_user_id(self, user_id: int):
        return self.wallet_repository.get_wallet_by_user_id(user_id)
    
    def create_wallet(self, user_id: int):
        wallet = WalletCreate(user_id=user_id, balance=0)
        return self.wallet_repository.create_wallet(wallet)
    
    def update_wallet(self, wallet: Wallet):
        return self.wallet_repository.update_wallet(wallet)
    
    def add_founds(self, user_id: int, amount: int):
        wallet = self.wallet_repository.get_wallet_by_user_id(user_id)
        wallet.balance += amount
        return self.wallet_repository.update_wallet(wallet)
    
    def remove_founds(self, user_id: int, amount: int):
        wallet = self.wallet_repository.get_wallet_by_user_id(user_id)
        if wallet is None:
            raise Exception("Wallet not found")
        if wallet.balance < amount:
            raise Exception("Not enough founds")
        wallet.balance -= amount
        return self.wallet_repository.update_wallet(wallet)
    
    def validate_founds(self, user_id: int, amount: int):
        wallet = self.wallet_repository.get_wallet_by_user_id(user_id)
        if wallet is None:
            raise Exception("Wallet not found")
        if wallet.balance < amount:
            raise Exception("Not enough founds")
        return True
    