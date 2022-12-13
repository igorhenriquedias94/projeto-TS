from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from api.deps import get_db
from business.wallet.model import Wallet, WalletUpdateFounds
from business.wallet.service import WalletService
from business.user.service import UserService
from business.transaction.service import TransactionService
from business.transaction.model import TransactionCreateReq, Transaction

router = InferringRouter()

@cbv(router)
class TransactionController:
    db:Session = Depends(get_db)
    
    @router.post("/", response_model=Transaction)
    async def create_transaction(self, transaction: TransactionCreateReq):
        user_service = UserService(self.db)
        transaction_service = TransactionService(self.db)
        return transaction_service.create_transaction(transaction)