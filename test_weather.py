from services.weather import get_weather

weather = get_weather("Goa")

print()

print("=" * 60)
print("Weather Forecast")
print("=" * 60)

for day in weather:

    print(day)