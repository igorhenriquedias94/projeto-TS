from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from business.item.model import Item, ItemCreate
from business.item.service import ItemService
from sqlalchemy.orm import Session
from api.deps import get_db

router = InferringRouter()

@cbv(router)
class ItemController:
    db:Session = Depends(get_db)
    
    @router.get("/")
    async def get_items(self, skip: int = 0, limit: int = 100):
        item_service = ItemService(self.db)
        return item_service.get_items_page(skip, limit)
    
    @router.post("/", response_model=Item)
    async def create_item(self, item: ItemCreate):
        item_service = ItemService(self.db)
        if item_service.get_item_by_name(item.name):
            raise HTTPException(status_code=400, detail="Item already registered")
        return item_service.create_item(item)
    
    @router.get("/{item_id}", response_model=Item)
    async def get_item(self, item_id: int):
        item_service = ItemService(self.db)
        db_item = item_service.get_item_by_id(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item
    
    @router.put("/{item_id}", response_model=Item)
    async def update_item(self, item_id: int, item: Item):
        item_service = ItemService(self.db)
        db_item = item_service.get_item_by_id(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item_service.update_item(item)
    
    @router.delete("/{item_id}", response_model=Item)
    async def delete_item(self, item_id: int):
        item_service = ItemService(self.db)
        db_item = item_service.get_item_by_id(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item_service.delete_item(item_id)