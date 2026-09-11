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
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as exc:
        raise RuntimeError(
            "The geocoding service returned an invalid response. "
            "Please try again shortly."
        ) from exc

    if not data:
        raise RuntimeError(f"Could not find coordinates for '{city}'.")

    return {
        "lat": float(data[0]["lat"]),
        "lon": float(data[0]["lon"])
    }
