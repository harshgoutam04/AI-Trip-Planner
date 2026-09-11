import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-20b"


def generate_itinerary(
    destination: str,
    days: int,
    budget_style: str,
    hotel_rating: int,
    transport_preference: str,
    food_preference: str,
    weather=None,
    attractions=None,
    hotel=None,
):
    """
    Generate a realistic itinerary using
    live weather, attractions and hotel.
    """

    # ----------------------------
    # Weather Summary
    # ----------------------------

    weather_summary = "Not Available"

    if weather:
        weather_summary = "\n".join(
            [
                f"{w.date}: {w.description}, {w.temperature}°C"
                for w in weather
            ]
        )

    # ----------------------------
    # Attractions Summary
    # ----------------------------

    attraction_summary = "Not Available"

    if attractions:
        attraction_summary = "\n".join(
            [
                f"- {a.name}"
                for a in attractions
            ]
        )

    # ----------------------------
    # Hotel Summary
    # ----------------------------

    hotel_summary = "No hotel selected."

    if hotel:
        hotel_summary = f"""
Recommended Hotel

Name:
{hotel.name}

Address:
{hotel.address}

Estimated Price:
₹{hotel.estimated_price}/night

This hotel should be used as the base for the itinerary.
"""

    # ----------------------------
    # Prompt
    # ----------------------------

    prompt = f"""
You are an expert travel planner.

Create a {days}-day itinerary for a trip to {destination}.

==========================
TRIP DETAILS
==========================

Budget Style:
{budget_style}

Hotel Rating:
{hotel_rating} Star

Transport Preference:
{transport_preference}

Food Preference:
{food_preference}

==========================
HOTEL
==========================

{hotel_summary}

==========================
WEATHER FORECAST
==========================

{weather_summary}

==========================
AVAILABLE ATTRACTIONS
==========================

{attraction_summary}

==========================
INSTRUCTIONS
==========================

- Divide the itinerary into Day 1, Day 2, etc.
- Include Morning, Afternoon and Evening.
- Start and end each day from the recommended hotel.
- Use ONLY the attractions listed above whenever possible.
- If rain is expected, avoid beaches and outdoor activities.
- Prefer museums, churches, shopping malls or indoor attractions on rainy days.
- Recommend realistic vegetarian/non-vegetarian restaurants according to the user's preference.
- Minimize unnecessary travelling between attractions.
- Keep activities geographically close together.
- Mention the recommended hotel only where appropriate (check-in/check-out or returning at night).
- Do NOT invent fake attractions.
- Do NOT invent fake hotels.
- Return clean Markdown only.
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.6,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content