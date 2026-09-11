from typing import TypedDict, List, Optional


class TripState(TypedDict):

    # User Input
    source: str
    destination: str
    start_date: str
    end_date: str

    travellers: int
    hotel_rating: int

    budget_style: str
    transport_preference: str
    food_preference: str

    # Conversation

    messages: List[dict]

    # API Results

    transport: Optional[list]
    hotels: Optional[list]
    attractions: Optional[list]
    weather: Optional[list]

    budget: Optional[dict]

    itinerary: Optional[str]

    # Agent

    next_step: Optional[str]

    missing: Optional[list]

    completed: bool