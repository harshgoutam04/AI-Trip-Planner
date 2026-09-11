import requests


def get_coordinates(city: str):
    """
    Returns latitude and longitude for a city.
    """

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "AI Trip Planner"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    data = response.json()

    if not data:
        return None

    return {
        "lat": float(data[0]["lat"]),
        "lon": float(data[0]["lon"])
    }