from sqlalchemy.orm import Session

from business.product_balance.dao import ProductBalanceDAO
from business.product_balance.model import ProductBalance, ProductBalanceCreate

class ProductBalanceRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_product_balance(self, skip: int = 0, limit: int = 100):
        return self.db.query(ProductBalanceDAO).offset(skip).limit(limit).all()


    def get_product_balance_by_user_id(self, user_id: int):
        return self.db.query(ProductBalanceDAO).filter(ProductBalanceDAO.user_id == user_id).all()


    def get_product_balance_by_user_id_and_item_id(self, user_id: int, item_id: int):
        return self.db.query(ProductBalanceDAO).filter(ProductBalanceDAO.user_id == user_id, ProductBalanceDAO.item_id == item_id).first()


    def create_product_balance(self, product_balance: ProductBalanceCreate):
        db_product_balance = ProductBalanceDAO(**product_balance.dict())
        self.db.add(db_product_balance)
        self.db.commit()
        self.db.refresh(db_product_balance)
        return db_product_balance


    def update_product_balance(self, product_balance: ProductBalance):
        db_product_balance = self.db.query(ProductBalanceDAO).filter(ProductBalanceDAO.user_id == product_balance.user_id, ProductBalanceDAO.item_id == product_balance.item_id).first()
        db_product_balance.balance = product_balance.balance
        self.db.commit()
        self.db.refresh(db_product_balance)
        return db_product_balance