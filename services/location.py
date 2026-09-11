import os
from functools import lru_cache

import openrouteservice
from dotenv import load_dotenv

load_dotenv()

client = openrouteservice.Client(
    key=os.getenv("OPENROUTESERVICE_API_KEY")
)


@lru_cache(maxsize=128)
def get_coordinates(city: str):
    """Return latitude and longitude for a city using OpenRouteService."""

    if not os.getenv("OPENROUTESERVICE_API_KEY"):
        raise RuntimeError("OPENROUTESERVICE_API_KEY is not configured.")

    result = client.pelias_search(text=city)
    features = result.get("features", [])

    if not features:
        raise RuntimeError(f"Could not find coordinates for '{city}'.")

    coordinates = features[0].get("geometry", {}).get("coordinates", [])

    if len(coordinates) < 2:
        raise RuntimeError(f"Could not find coordinates for '{city}'.")

    return {
        "lat": float(coordinates[1]),
        "lon": float(coordinates[0]),
    }
