from sqlalchemy.orm import Session

from .dao import WalletDAO
from .model import Wallet, WalletCreate


class WalletRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_wallet(self, skip: int = 0, limit: int = 100):
        return self.db.query(WalletDAO).offset(skip).limit(limit).all()


    def get_wallet_by_user_id(self, user_id: int):
        return self.db.query(WalletDAO).filter(WalletDAO.user_id == user_id).first()


    def create_wallet(self, wallet: WalletCreate):
        db_wallet = WalletDAO(**wallet.dict())
        self.db.add(db_wallet)
        self.db.commit()
        self.db.refresh(db_wallet)
        return db_wallet


    def update_wallet(self, wallet: Wallet):
        db_wallet = self.db.query(WalletDAO).filter(WalletDAO.user_id == wallet.user_id).first()
        db_wallet.balance = wallet.balance
        self.db.commit()
        self.db.refresh(db_wallet)
        return db_wallet
