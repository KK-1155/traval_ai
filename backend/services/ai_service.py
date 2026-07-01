import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_itinerary(
    start_city,
    destination,
    vibe,
    duration,
    budget,
    weather
):
    try:

        prompt = f"""
You are a Myanmar travel expert.

Create a detailed {duration}-day travel itinerary.

Start City:
{start_city}

Destination:
{destination}

Travel Style:
{vibe}

Budget:
{budget} MMK

Weather:
{weather}

Requirements:

1. Day by Day Plan
2. Attractions
3. Local Foods
4. Travel Tips
5. Estimated Daily Spending

Return in markdown format.
"""

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"