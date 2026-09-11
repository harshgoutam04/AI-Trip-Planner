import json
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "qwen/qwen3.8-27b"


def ask_llm(messages):
    """
    Normal conversation with the AI.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.3,
        max_completion_tokens=1024,
    )

    return response.choices[0].message.content


def extract_trip_information(user_message: str):
    """
    Extracts structured trip information from
    the user's message.
    """

    system_prompt = """
You are an information extraction assistant.

Your job is ONLY to extract trip information.

Return ONLY valid JSON.

Never explain anything.

Never use markdown.

If a value is missing return null.

JSON format:

{
    "source": null,
    "destination": null,
    "start_date": null,
    "end_date": null,
    "travellers": null,
    "hotel_rating": null,
    "budget_style": null,
    "transport_preference": null,
    "food_preference": null
}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        max_completion_tokens=512,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)

    except Exception:
        return {
            "source": None,
            "destination": None,
            "start_date": None,
            "end_date": None,
            "travellers": None,
            "hotel_rating": None,
            "budget_style": None,
            "transport_preference": None,
            "food_preference": None
        }