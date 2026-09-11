from services.hotels import search_hotels

hotels = search_hotels("Hyderabad")

print()

print("=" * 60)
print(f"Found {len(hotels)} Hotels")
print("=" * 60)

for hotel in hotels:

    print()

    print(hotel.name)
    print(hotel.address)
    print(hotel.distance, "meters")
    print(hotel.website)

    print("-" * 50)