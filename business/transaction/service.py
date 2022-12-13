from business.transaction.repository import TransactionRepository
from business.transaction.model import TransactionCreateReq, Transaction, TransactionCreate
from business.wallet.service import WalletService
from business.user.service import UserService
from business.product_balance.service import ProductBalanceService
from business.item.service import ItemService
from sqlalchemy.orm import Session

class TransactionService():
    def __init__(self, db: Session):
        self.transaction_repository = TransactionRepository(db)
        self.user_service = UserService(db)
        self.product_balance_service = ProductBalanceService(db)
        self.wallet_service = WalletService(db)
        self.item_service = ItemService(db)
        
    def get_transactions(self, skip: int, limit: int):
        return self.transaction_repository.get_transactions(skip, limit)
    
    def get_transactions_by_user_id(self, user_id: int):
        return self.transaction_repository.get_transactions_by_user_id(user_id)
    
    def create_transaction(self, transaction: TransactionCreateReq):
        self.validate_transaction(transaction)
        item = self.item_service.get_item_by_id(transaction.item_id)
        transaction_to_save = TransactionCreate(**transaction.dict(), price = item.price * transaction.balance)
        transaction = self.transaction_repository.create_transaction(transaction_to_save)
        
        self.wallet_service.remove_founds(transaction.buyer_id, transaction.balance * item.price)
        self.wallet_service.add_founds(transaction.seller_id, transaction.balance * item.price)
        
        self.product_balance_service.add_product_amount(transaction.buyer_id, transaction.item_id, transaction.balance)
        self.product_balance_service.remove_product_amount(transaction.seller_id, transaction.item_id, transaction.balance)
        return transaction
    
    def validate_transaction(self, transaction: Transaction):
        if transaction.buyer_id == transaction.seller_id:
            raise Exception("Buyer and seller cannot be the same")
        if transaction.balance <= 0:
            raise Exception("Balance must be greater than 0")
        buyer = self.user_service.get_user(transaction.buyer_id)
        if buyer is None:
            raise Exception("Buyer not found")
        seller = self.user_service.get_user(transaction.seller_id)
        if seller is None:
            raise Exception("Seller not found")
        item = self.item_service.get_item_by_id(transaction.item_id)
        if item is None:
            raise Exception("Item not found")
        self.wallet_service.validate_founds(transaction.buyer_id, transaction.balance * item.price)
        self.product_balance_service.validate_product_amount(transaction.seller_id, transaction.item_id, transaction.balance)
        return True