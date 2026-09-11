from datetime import datetime

from agent.state import TripState

from services.transport import search_transport
from services.hotels import search_hotels
from services.attractions import search_attractions
from services.weather import get_weather
from services.budget import estimate_budget
from services.itinerary import generate_itinerary


def calculate_nights(start_date, end_date):
    """
    Calculate number of nights between two dates.
    """

    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")

    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    nights = (end_date - start_date).days

    return max(nights, 1)


def run_trip_planner(state: TripState):
    """
    Executes the complete trip planning pipeline.
    """

    # ======================================================
    # Transport
    # ======================================================

    transport_options = search_transport(
        state["source"],
        state["destination"],
    )

    state["transport"] = transport_options

    selected_transport = transport_options[0]

    transport_price = selected_transport.estimated_price

    # ======================================================
    # Hotels
    # ======================================================

    hotels = search_hotels(
        city=state["destination"],
        hotel_rating=state["hotel_rating"],
    )

    state["hotels"] = hotels

    selected_hotel = hotels[0] if hotels else None

    state["selected_hotel"] = selected_hotel

    # ======================================================
    # Attractions
    # ======================================================

    attractions = search_attractions(
        state["destination"]
    )

    state["attractions"] = attractions

    # ======================================================
    # Weather
    # ======================================================

    weather = get_weather(
        state["destination"]
    )

    state["weather"] = weather

    # ======================================================
    # Trip Duration
    # ======================================================

    nights = calculate_nights(
        state["start_date"],
        state["end_date"],
    )

    # ======================================================
    # Hotel Price
    # ======================================================

    if selected_hotel:
        hotel_price = selected_hotel.estimated_price
    else:
        hotel_price = 3000

    # ======================================================
    # Budget
    # ======================================================

    budget = estimate_budget(
        transport_cost=transport_price,
        hotel_price_per_night=hotel_price,
        nights=nights,
        travellers=state["travellers"],
        budget_style=state["budget_style"],
    )

    state["budget"] = budget

    # ======================================================
    # Itinerary
    # ======================================================

    itinerary = generate_itinerary(
        destination=state["destination"],
        days=nights + 1,
        budget_style=state["budget_style"],
        hotel_rating=state["hotel_rating"],
        transport_preference=state["transport_preference"],
        food_preference=state["food_preference"],
        weather=weather,
        attractions=attractions,
        hotel=selected_hotel,
    )

    state["itinerary"] = itinerary

    # ======================================================
    # Completed
    # ======================================================

    state["completed"] = True

    return state