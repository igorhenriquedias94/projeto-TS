from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from api.deps import get_db
from business.user.service import UserService
from business.product_balance.model import ProductBalance, ProductBalanceUpdateAmount
from business.product_balance.service import ProductBalanceService

router = InferringRouter()

@cbv(router)
class ProductBalanceController:
    db:Session = Depends(get_db)
    
    @router.post("/{user_id}/add-product", response_model=ProductBalance)
    async def add_product(self, user_id: int, product: ProductBalanceUpdateAmount):
        user_service = UserService(self.db)
        product_balance_service = ProductBalanceService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return product_balance_service.add_product_amount(user_id, product.item_id, product.amount)
    
    @router.post("/{user_id}/remove-product", response_model=ProductBalance)
    async def remove_product(self, user_id: int, product: ProductBalanceUpdateAmount):
        user_service = UserService(self.db)
        product_balance_service = ProductBalanceService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return product_balance_service.remove_product_amount(user_id, product.item_id, product.amount)
    