from services.budget import estimate_budget

budget = estimate_budget(
    transport_cost=5750,
    hotel_price_per_night=5500,
    nights=5,
    travellers=2,
    budget_style="Comfort",
)

print(budget)