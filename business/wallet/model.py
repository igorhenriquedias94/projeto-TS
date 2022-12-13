from pydantic import BaseModel

class WalletBase(BaseModel):
    user_id: int
    balance: int
    

class WalletCreate(WalletBase):
    pass


class Wallet(WalletBase):
    id: int

    class Config:
        orm_mode = True
        

class WalletUpdateFounds(BaseModel):
    user_id: int
    amount: int