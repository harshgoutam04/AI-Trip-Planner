from agent.graph import trip_graph

state = {
    "messages": [],

    "source": "Delhi",
    "destination": "Goa",

    "start_date": "2026-10-10",
    "end_date": "2026-10-15",

    "travellers": 3,

    "hotel_rating": 4,
    "budget_style": "Comfort",
    "transport_preference": "Fastest",
    "food_preference": "Vegetarian",

    "transport": None,
    "hotels": None,
    "attractions": None,
    "weather": None,
    "budget": None,
    "itinerary": None,

    "missing_fields": [],
    "completed": False,
}

result = trip_graph.invoke(state)

print("=" * 60)
print("Completed:", result["completed"])

print("=" * 60)
print("Transport")
print(result["transport"])

print("=" * 60)
print("Hotels")
print(result["hotels"])

print("=" * 60)
print("Weather")
print(result["weather"])

print("=" * 60)
print("Attractions")
print(result["attractions"][:5])

print("=" * 60)
print("Budget")
print(result["budget"])

print("=" * 60)
print("Itinerary")
print(result["itinerary"][:1200])