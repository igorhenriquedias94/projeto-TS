from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from api.deps import get_db
from business.wallet.model import Wallet, WalletUpdateFounds
from business.wallet.service import WalletService
from business.user.service import UserService

router = InferringRouter()

@cbv(router)
class WalletController:
    db:Session = Depends(get_db)
    
    @router.post("/{user_id}/add-founds", response_model=Wallet)
    async def add_founds(self, user_id: int, wallet: WalletUpdateFounds):
        user_service = UserService(self.db)
        wallet_service = WalletService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return wallet_service.add_founds(user_id, wallet.amount)
    
    @router.post("/{user_id}/remove-founds", response_model=Wallet)
    async def remove_founds(self, user_id: int, wallet: WalletUpdateFounds):
        user_service = UserService(self.db)
        wallet_service = WalletService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return wallet_service.remove_founds(user_id, wallet.amount)
        