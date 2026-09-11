from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TransportOption:
    mode: str
    duration: str
    estimated_price: int
    booking_link: str
    best_for: str


@dataclass
class HotelOption:
    destination: str
    hotel_rating: int
    average_price: int
    booking_link: str
    maps_link: str


@dataclass
class BudgetSummary:
    transport: int
    hotel: int
    food: int
    local_transport: int
    miscellaneous: int
    grand_total: int
    per_person: float


@dataclass
class TripPlan:

    source: str
    destination: str

    transport: List[TransportOption] = field(default_factory=list)

    hotel: Optional[HotelOption] = None

    budget: Optional[BudgetSummary] = None

    itinerary: Optional[str] = None