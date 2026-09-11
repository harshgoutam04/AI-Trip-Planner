from services.attractions import search_attractions

places = search_attractions("Hyderabad")

print()

print("=" * 60)
print("Attractions Found")
print("=" * 60)

for place in places:

    print()

    print(place.name)

    print(place.category)

    print(place.distance)

    print("-" * 50)