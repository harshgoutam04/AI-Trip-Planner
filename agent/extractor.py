from agent.state import TripState
from utils.llm import extract_trip_information


def extract_trip_state(user_message: str) -> TripState:
    """
    Converts user text into TripState.
    """

    extracted = extract_trip_information(user_message)

    trip = TripState(
        source=extracted.get("source"),
        destination=extracted.get("destination"),
        start_date=extracted.get("start_date"),
        end_date=extracted.get("end_date"),
        travellers=extracted.get("travellers"),
        hotel_rating=extracted.get("hotel_rating"),
        budget_style=extracted.get("budget_style"),
        transport_preference=extracted.get("transport_preference"),
        food_preference=extracted.get("food_preference"),
    )

    return trip 