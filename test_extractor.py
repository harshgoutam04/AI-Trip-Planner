from agent.extractor import extract_trip_state

trip = extract_trip_state(
    """
I'm planning a trip from Delhi to Goa from 10 October to 15 October.

There will be 2 people.

We want a 4 star hotel.

We prefer the cheapest transport.
"""
)

print("\n========== EXTRACTED TRIP ==========\n")

print(trip)

print("\n===================================\n")