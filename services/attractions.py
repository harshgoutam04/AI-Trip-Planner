import requests

from utils.config import OPENTRIPMAP_API_KEY
from services.location import get_coordinates
from schemas.attraction import Attraction


def search_attractions(
    city: str,
    radius: int = 10000,
    limit: int = 20,
):

    coords = get_coordinates(city)

    lat = coords["lat"]
    lon = coords["lon"]

    url = "https://api.opentripmap.com/0.1/en/places/radius"

    params = {
        "apikey": OPENTRIPMAP_API_KEY,
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "limit": limit,
        "rate": 2,
        "format": "json",
    }

    response = requests.get(
        url,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    attractions = []

    seen = set()

    for place in data:

        name = place.get("name", "").strip()

        if not name:
            continue

        if name in seen:
            continue

        seen.add(name)

        attractions.append(

            Attraction(

                name=name,

                category=place.get("kinds", ""),

                latitude=place["point"]["lat"],

                longitude=place["point"]["lon"],

                distance=place.get("dist"),

                wikipedia=place.get("wikipedia"),

                osm=place.get("osm"),

            )

        )

    attractions.sort(
        key=lambda x: x.distance
    )

    return attractions