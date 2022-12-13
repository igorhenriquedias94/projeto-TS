from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from business.database.database import Base
from business.database.database import engine

from api.endpoints.user import router as user_router
from api.endpoints.item import router as item_router
from api.endpoints.wallet import router as wallet_router
from api.endpoints.product_balance import router as product_balance_router
from api.endpoints.transaction import router as transaction_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(item_router, prefix="/item", tags=["item"])
app.include_router(wallet_router, prefix="/wallet", tags=["wallet"])
app.include_router(product_balance_router, prefix="/product-balance", tags=["product-balance"])
app.include_router(transaction_router, prefix="/transaction", tags=["transaction"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
