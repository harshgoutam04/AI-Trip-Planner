import os

import openrouteservice
from dotenv import load_dotenv

from services.location import get_coordinates

load_dotenv()

client = openrouteservice.Client(
    key=os.getenv("OPENROUTESERVICE_API_KEY")
)


def get_route(source: str, destination: str):
    """
    Returns driving distance and duration.
    """

    source_coord = get_coordinates(source)
    dest_coord = get_coordinates(destination)

    coords = [
        (source_coord["lon"], source_coord["lat"]),
        (dest_coord["lon"], dest_coord["lat"]),
    ]

    route = client.directions(
        coords,
        profile="driving-car",
        format="geojson",
    )

    summary = route["features"][0]["properties"]["summary"]

    return {
        "distance_km": round(summary["distance"] / 1000, 1),
        "duration_hr": round(summary["duration"] / 3600, 1),
    }