from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.db.models.inventory import InventoryItem
from app.api.routes.inventory import router as inventory_router

app = FastAPI(title="StockPilot API")

Base.metadata.create_all(bind=engine)

app.include_router(inventory_router)

@app.get("/")
def health_check():
    return {"status": "StockPilot running"}