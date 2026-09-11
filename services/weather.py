import requests

from utils.config import OPENWEATHER_API_KEY
from services.location import get_coordinates
from schemas.weather import WeatherForecast


def get_weather(city: str):

    coords = get_coordinates(city)

    lat = coords["lat"]
    lon = coords["lon"]

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }

    response = requests.get(
        url,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    forecasts = []

    seen_dates = set()

    for item in data["list"]:

        date = item["dt_txt"].split()[0]

        # Keep only one forecast per day (around every 24h)
        if date in seen_dates:
            continue

        seen_dates.add(date)

        forecasts.append(

            WeatherForecast(

                date=date,

                temperature=item["main"]["temp"],

                feels_like=item["main"]["feels_like"],

                description=item["weather"][0]["description"],

                humidity=item["main"]["humidity"],

                wind_speed=item["wind"]["speed"],

            )

        )

    return forecasts