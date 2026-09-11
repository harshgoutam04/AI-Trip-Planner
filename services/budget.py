from schemas.trip import BudgetSummary


def estimate_budget(
    transport_cost: int,
    hotel_price_per_night: int,
    nights: int,
    travellers: int,
    budget_style: str,
):
    """
    Estimate the total trip budget.
    """

    # Food cost per person per day
    food_cost = {
        "Backpacker": 700,
        "Comfort": 1500,
        "Luxury": 3000,
    }

    # Local transport per day
    local_transport = {
        "Backpacker": 400,
        "Comfort": 800,
        "Luxury": 1800,
    }

    food_per_day = food_cost.get(
        budget_style,
        1500,
    )

    local_per_day = local_transport.get(
        budget_style,
        800,
    )

    hotel_total = hotel_price_per_night * nights

    food_total = (
        food_per_day
        * travellers
        * nights
    )

    local_total = (
        local_per_day
        * travellers
        * nights
    )

    transport_total = (
        transport_cost
        * travellers
    )

    subtotal = (
        transport_total
        + hotel_total
        + food_total
        + local_total
    )

    miscellaneous = int(
        subtotal * 0.10
    )

    grand_total = (
        subtotal
        + miscellaneous
    )

    per_person = (
        grand_total / travellers
    )

    return BudgetSummary(
        transport=transport_total,
        hotel=hotel_total,
        food=food_total,
        local_transport=local_total,
        miscellaneous=miscellaneous,
        grand_total=grand_total,
        per_person=per_person,
    )