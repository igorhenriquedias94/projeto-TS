from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None
    price: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True