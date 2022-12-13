from pydantic import BaseModel

class TransactionBase(BaseModel):
    item_id: int
    buyer_id: int
    seller_id: int
    balance: int


class TransactionCreateReq(TransactionBase):
    pass


class TransactionCreate(TransactionBase):
    price: int
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True