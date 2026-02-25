from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InventoryCreate(BaseModel):
    name: str
    sku: str
    quantity: int
    reorder_level: int
    unit_cost: float

class InventoryResponse(BaseModel):
    id: int
    name: str
    sku: str
    quantity: int
    reorder_level: int
    unit_cost: float
    created_at: datetime

    class Config:
        from_attributes = True