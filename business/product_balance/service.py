from .repository import ProductBalanceCreate, ProductBalance, ProductBalanceRepository
from sqlalchemy.orm import Session

class ProductBalanceService():
    def __init__(self, db: Session):
        self.product_balance_repository = ProductBalanceRepository(db)

    def get_product_balance_by_user_id_and_item_id(self, user_id: int, item_id: int):
        return self.product_balance_repository.get_product_balance_by_user_id_and_item_id(user_id, item_id)
    
    def update_product_balance(self, product_balance: ProductBalance):
        return self.product_balance_repository.update_product_balance(product_balance)
    
    def create_product_balance(self, product_balance: ProductBalanceCreate):
        return self.product_balance_repository.create_product_balance(product_balance)

    def add_product_amount(self, user_id: int, item_id: int, amount: int):
        product_balance = self.get_product_balance_by_user_id_and_item_id(user_id, item_id)
        if product_balance:
            product_balance.balance += amount
            return self.update_product_balance(product_balance)
        else:
            product_balance = ProductBalanceCreate(user_id=user_id, item_id=item_id, balance=amount)
            return self.create_product_balance(product_balance)

    def remove_product_amount(self, user_id: int, item_id: int, amount: int):
        product_balance = self.get_product_balance_by_user_id_and_item_id(user_id, item_id)
        if product_balance is None:
            raise Exception("Product balance not found")
        if product_balance.balance < amount:
            raise Exception("Not enough product amount")
        product_balance.balance -= amount
        return self.update_product_balance(product_balance)
    
    def validate_product_amount(self, user_id: int, item_id: int, amount: int):
        product_balance = self.get_product_balance_by_user_id_and_item_id(user_id, item_id)
        if product_balance is None:
            raise Exception("Product balance not found")
        if product_balance.balance < amount:
            raise Exception("Not enough product amount")
        return True
            