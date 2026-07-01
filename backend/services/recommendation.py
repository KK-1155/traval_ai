import json
from pathlib import Path

DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "destinations.json"
)


def get_destinations(
    vibe,
    budget
):

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        destinations = data.get(
            vibe,
            []
        )

        if budget < 300000:

            return destinations[:2]

        elif budget < 1000000:

            return destinations[:3]

        else:

            return destinations

    except Exception as e:

        print(
            "Recommendation Error:",
            e
        )

        return []