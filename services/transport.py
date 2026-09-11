import os

from groq import Groq
from dotenv import load_dotenv

from schemas.transport import TransportOption
from services.routes import get_route

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-20b"


def search_transport(source: str, destination: str):
    """
    Uses OpenRouteService + LLM to generate realistic transport options.
    """

    route = get_route(source, destination)

    distance = route["distance_km"]
    drive_time = route["duration_hr"]

    prompt = f"""
You are a travel assistant.

Trip:

Source: {source}

Destination: {destination}

Driving Distance:
{distance:.1f} km

Driving Time:
{drive_time:.1f} hours

Generate exactly FOUR transport options.

Return ONLY valid JSON.

Example:

[
 {{
   "mode":"Flight",
   "duration":"2h 30m",
   "estimated_price":6500,
   "booking_link":"https://www.google.com/travel/flights",
   "best_for":"Fastest"
 }},
 {{
   "mode":"Train",
   "duration":"28h",
   "estimated_price":2200,
   "booking_link":"https://www.irctc.co.in",
   "best_for":"Budget"
 }},
 {{
   "mode":"Bus",
   "duration":"30h",
   "estimated_price":1700,
   "booking_link":"https://www.redbus.in",
   "best_for":"Cheapest"
 }},
 {{
   "mode":"Car",
   "duration":"{drive_time:.1f}h",
   "estimated_price":{int(distance*8)},
   "booking_link":"https://www.uber.com",
   "best_for":"Flexible"
 }}
]

Do not write markdown.
Do not explain anything.
Only JSON.
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    import json

    data = json.loads(response.choices[0].message.content)

    if isinstance(data, dict):
        options = data.get("transport", [])
    else:
        options = data

    return [TransportOption(**item) for item in options]