from typing import Optional
from pydantic import BaseModel


class Hotel(BaseModel):
    name: str
    address: str

    latitude: float
    longitude: float

    distance: float

    website: Optional[str] = None

    category: str
    city: str

    estimated_price: int