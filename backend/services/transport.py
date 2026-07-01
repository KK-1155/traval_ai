import json
from pathlib import Path

DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "transport.json"
)


def recommend_transport(
    start_city,
    destination,
    budget
):

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            routes = json.load(f)

        route = (
            f"{start_city}-{destination}"
        )

        data = routes.get(route)

        if not data:

            return {
                "type": "Bus",
                "cost": 50000
            }

        if budget < 500000:

            return {
                "type": "Bus",
                "cost": data["bus"]
            }

        return {
            "type": "Flight",
            "cost": data["flight"]
        }

    except Exception:

        return {
            "type": "Bus",
            "cost": 50000
        }