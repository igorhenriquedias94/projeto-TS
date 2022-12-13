from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from business.user.model import User, UserCreate
from business.user.service import UserService
from sqlalchemy.orm import Session
from api.deps import get_db

router = InferringRouter()

@cbv(router)
class UserController:
    db:Session = Depends(get_db)
    
    @router.get("/")
    async def get_users(self, skip: int = 0, limit: int = 100):
        user_service = UserService(self.db)
        return user_service.get_users_page(skip, limit)
    
    @router.post("/", response_model=User)
    async def create_user(self, user: UserCreate):
        user_service = UserService(self.db)
        db_user = user_service.get_user_by_email(user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return user_service.create_user_with_wallet(user)
    
    @router.get("/{user_id}", response_model=User)
    async def get_user(self, user_id: int):
        user_service = UserService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    
    @router.put("/{user_id}", response_model=User)
    async def update_user(self, user_id: int, user: User):
        user_service = UserService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user_service.update_user(user)
    
    @router.delete("/{user_id}", response_model=User)
    async def delete_user(self, user_id: int):
        user_service = UserService(self.db)
        db_user = user_service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user_service.delete_user(user_id)
