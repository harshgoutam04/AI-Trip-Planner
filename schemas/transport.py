from pydantic import BaseModel


class TransportOption(BaseModel):
    mode: str
    duration: str
    estimated_price: int
    booking_link: str
    best_for: str