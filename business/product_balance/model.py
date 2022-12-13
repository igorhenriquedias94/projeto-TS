from pydantic import BaseModel


class ProductBalanceBase(BaseModel):
    user_id: int
    item_id: int
    balance: int


class ProductBalanceCreate(ProductBalanceBase):
    pass


class ProductBalance(ProductBalanceBase):
    id: int

    class Config:
        orm_mode = True
        

class ProductBalanceUpdateAmount(BaseModel):
    user_id: int
    item_id: int
    amount: int