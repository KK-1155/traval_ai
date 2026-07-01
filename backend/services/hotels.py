import json
from pathlib import Path

DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "hotels.json"
)


def recommend_hotel(
    destination,
    budget
):
    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            hotels = json.load(f)

        city_hotels = hotels.get(
            destination,
            {}
        )

        if budget < 300000:

            return city_hotels.get(
                "budget",
                {
                    "name": "Budget Hotel",
                    "price": 25000
                }
            )

        elif budget < 1000000:

            return city_hotels.get(
                "standard",
                {
                    "name": "Standard Hotel",
                    "price": 70000
                }
            )

        else:

            return city_hotels.get(
                "luxury",
                {
                    "name": "Luxury Hotel",
                    "price": 200000
                }
            )

    except Exception as e:

        return {
            "name": f"Error: {e}",
            "price": 0
        }