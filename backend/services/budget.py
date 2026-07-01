def calculate_trip_cost(
    duration,
    hotel_price,
    transport_cost
):

    food_cost = (
        25000 * duration
    )

    hotel_cost = (
        hotel_price * duration
    )

    activity_cost = (
        20000 * duration
    )

    total_cost = (
        hotel_cost
        + food_cost
        + transport_cost
        + activity_cost
    )

    return {

        "hotel_cost":
        hotel_cost,

        "food_cost":
        food_cost,

        "activity_cost":
        activity_cost,

        "transport_cost":
        transport_cost,

        "total_cost":
        total_cost
    }