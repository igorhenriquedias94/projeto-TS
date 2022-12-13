from sqlalchemy.orm import Session

from business.transaction.dao import TransactionDAO
from business.transaction.model import TransactionCreate


class TransactionRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_transactions(self, skip: int = 0, limit: int = 100):
        return self.db.query(TransactionDAO).offset(skip).limit(limit).all()

    def get_transactions_by_user_id(self, user_id: int):
        buyer = self.db.query(TransactionDAO).filter(TransactionDAO.buyer_id == user_id).all()
        seller = self.db.query(TransactionDAO).filter(TransactionDAO.seller_id == user_id).all()
        return buyer + seller

    def create_transaction(self, transaction: TransactionCreate):
        db_transaction = TransactionDAO(**transaction.dict())
        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)
        return db_transaction
