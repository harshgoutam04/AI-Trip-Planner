from agent.nodes import validate_trip


state = {

    "source": "Delhi",

    "destination": "Hyderabad",

    "start_date": "2026-10-11",

    "end_date": "2026-10-15",

    "travellers": None,

    "hotel_rating": 4,

    "budget_style": "Comfort",

    "transport_preference": "Fastest",

    "food_preference": "Vegetarian",

    "messages": [],

    "transport": None,

    "hotels": None,

    "attractions": None,

    "weather": None,

    "budget": None,

    "itinerary": None,

    "next_step": None,

    "completed": False,

}

state = validate_trip(state)

print(state["next_step"])

print(state["missing"])