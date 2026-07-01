import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    if not API_KEY:
        return "Weather API Key Missing"

    try:

        url = "https://api.weatherapi.com/v1/current.json"

        response = requests.get(
            url,
            params={
                "key": API_KEY,
                "q": city,
                "aqi": "no"
            },
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        temp = data["current"]["temp_c"]

        condition = data["current"]["condition"]["text"]

        return f"{condition}, {temp}°C"

    except requests.exceptions.RequestException as e:

        print("Weather API Error:", e)

        return "Weather Unavailable"