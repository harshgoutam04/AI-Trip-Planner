from agent.state import TripState


def validate_trip(state: TripState):

    required = [
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

    missing = []

    for field in required:

        value = state.get(field)

        if value is None:
            missing.append(field)

        elif isinstance(value, str) and value.strip() == "":
            missing.append(field)

    if missing:

        state["next_step"] = "ask_user"

        state["missing"] = missing

    else:

        state["next_step"] = "plan_trip"

    return state