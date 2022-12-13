from sqlalchemy.orm import Session

from .dao import ItemDAO
from .model import Item, ItemCreate

class ItemRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(ItemDAO).offset(skip).limit(limit).all()
    
    def get_item_by_id(self, item_id: int):
        return self.db.query(ItemDAO).filter(ItemDAO.id == item_id).first()
    
    def get_item_by_name(self, name: str):
        return self.db.query(ItemDAO).filter(ItemDAO.name == name).first()

    def create_item(self, item: ItemCreate):
        db_item = ItemDAO(**item.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update_item(self, item: Item):
        db_item = self.db.query(ItemDAO).filter(ItemDAO.id == item.id).first()
        db_item.name = item.name
        db_item.description = item.description
        db_item.price = item.price
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def delete_item(self, item_id: int):
        db_item = self.db.query(ItemDAO).filter(ItemDAO.id == item_id).first()
        self.db.delete(db_item)
        self.db.commit()
        return db_item
