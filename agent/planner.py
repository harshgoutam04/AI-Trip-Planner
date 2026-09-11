from agent.state import TripState


REQUIRED_FIELDS = [
    "source",
    "destination",
    "start_date",
    "end_date",
    "travellers",
    "hotel_rating",
    "budget_style",
    "transport_preference",
    "food_preference",
]


def check_missing_fields(state: TripState) -> TripState:
    """
    Check which required trip details are still missing.
    """

    missing = []

    for field in REQUIRED_FIELDS:

        value = state.get(field)

        if value is None:
            missing.append(field)

        elif isinstance(value, str) and value.strip() == "":
            missing.append(field)

    state["missing_fields"] = missing

    state["completed"] = len(missing) == 0

    return state