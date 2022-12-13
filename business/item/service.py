from .repository import ItemRepository, ItemCreate, Item
from sqlalchemy.orm import Session

class ItemService():
    def __init__(self, db: Session):
        self.item_repository = ItemRepository(db)
        
    def get_item_by_id(self, item_id: int):
        return self.item_repository.get_item_by_id(item_id)
        
    def get_item_by_name(self, name: str):
        return self.item_repository.get_item_by_name(name)
        
    def get_items_page(self, skip: int, limit: int):
        return self.item_repository.get_items(skip, limit)
    
    def create_item(self, item: ItemCreate):
        return self.item_repository.create_item(item)
    
    def update_item(self, item: Item):
        return self.item_repository.update_item(item)
    
    def delete_item(self, item_id: int):
        return self.item_repository.delete_item(item_id)