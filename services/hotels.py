import os
import requests

from dotenv import load_dotenv

from schemas.hotel import Hotel
from services.location import get_coordinates

load_dotenv()

API_KEY = os.getenv("GEOAPIFY_API_KEY")


HOTEL_KEYWORDS = [
    "hotel",
    "resort",
    "inn",
    "lodge",
    "residency",
    "suite",
    "guest house",
    "guesthouse",
    "hostel",
]


def is_hotel(name: str) -> bool:
    """
    Returns True if the place looks like a hotel.
    """

    if not name:
        return False

    name = name.lower()

    return any(keyword in name for keyword in HOTEL_KEYWORDS)


def estimate_price(hotel_rating: int) -> int:
    """
    Temporary hotel price estimation.

    Later this can be replaced with Booking.com,
    Google Hotels, Expedia, etc.
    """

    prices = {
        3: 2500,
        4: 4500,
        5: 8500,
    }

    return prices.get(hotel_rating, 3000)


def search_hotels(
    city: str,
    hotel_rating: int = 4,
    radius: int = 6000,
    limit: int = 30,
):
    """
    Search nearby hotels using Geoapify.
    """

    coords = get_coordinates(city)

    lat = coords["lat"]
    lon = coords["lon"]

    url = "https://api.geoapify.com/v2/places"

    params = {
        "categories": "accommodation",
        "filter": f"circle:{lon},{lat},{radius}",
        "bias": f"proximity:{lon},{lat}",
        "limit": limit,
        "apiKey": API_KEY,
    }

    response = requests.get(
        url,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    hotels = []

    seen = set()

    for place in data.get("features", []):

        props = place["properties"]

        name = props.get("name", "")

        if not is_hotel(name):
            continue

        if name in seen:
            continue

        seen.add(name)

        hotels.append(
            Hotel(
                name=name,
                address=props.get("formatted", ""),
                latitude=props.get("lat"),
                longitude=props.get("lon"),
                distance=props.get("distance"),
                website=props.get("website"),
                category=props.get("categories", [None])[0],
                city=city,
                estimated_price=estimate_price(hotel_rating),
            )
        )

    hotels.sort(
        key=lambda hotel: hotel.distance if hotel.distance else 999999
    )

    return hotels