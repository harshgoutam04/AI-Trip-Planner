from services.transport import search_transport

transport = search_transport(
    "Hyderabad",
    "Goa",
)

for option in transport:
    print(option)