from agent.tools import run_trip_planner

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

state = run_trip_planner(state)

print("=" * 60)

print("TRANSPORT")

print(state["transport"])

print("=" * 60)

print("HOTEL")

print(state["hotel"])

print("=" * 60)

print("BUDGET")

print(state["budget"])

print("=" * 60)

print("ITINERARY")

print(state["itinerary"])