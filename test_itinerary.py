from services.itinerary import generate_itinerary

plan = generate_itinerary(
    destination="Goa",
    days=4,
    budget_style="Comfort",
    hotel_rating=4,
    transport_preference="Fastest",
    food_preference="Vegetarian",
)

print(plan)