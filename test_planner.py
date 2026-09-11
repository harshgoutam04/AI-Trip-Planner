from agent.planner import check_missing_fields

state = {
    "messages": [],

    "source": "Delhi",

    "destination": "Goa",

    "start_date": "2026-10-10",

    "end_date": "2026-10-15",

    "travellers": 2,

    "hotel_rating": 4,

    "budget_style": "Comfort",

    "transport_preference": "Fastest",

    "food_preference": "Vegetarian",

    "transport": None,

    "hotel": None,

    "budget": None,

    "itinerary": None,

    "missing_fields": [],

    "completed": False,
}

state = check_missing_fields(state)

print(state["missing_fields"])

print()

print(state["completed"])