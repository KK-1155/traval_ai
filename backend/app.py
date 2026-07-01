from fastapi import FastAPI
from pydantic import BaseModel

# အစက်ကလေးတွေ (.) ပြန်ဖြုတ်ပြီး ဒီအတိုင်း ရေးပေးပါ
from services.recommendation import get_destinations
from services.weather import get_weather
from services.hotels import recommend_hotel
from services.transport import recommend_transport
from services.budget import calculate_trip_cost
from services.ai_service import generate_itinerary

app = FastAPI(
    title="Myanmar AI Travel Planner"
)


class RecommendRequest(BaseModel):
    start_city: str
    vibe: str
    budget: int


class PlanRequest(BaseModel):
    start_city: str
    destination: str
    vibe: str
    budget: int
    duration: int


@app.get("/")
def root():
    return {
        "message": "Myanmar AI Travel Planner API Running"
    }


@app.post("/recommend")
def recommend(req: RecommendRequest):

    destinations = get_destinations(
        req.vibe,
        req.budget
    )

    return {
        "vibe": req.vibe,
        "budget": req.budget,
        "destinations": destinations
    }


@app.post("/generate-plan")
def generate_plan(req: PlanRequest):

    weather = get_weather(
        req.destination
    )

    hotel = recommend_hotel(
        req.destination,
        req.budget
    )

    transport = recommend_transport(
        req.start_city,
        req.destination,
        req.budget
    )

    costs = calculate_trip_cost(
        duration=req.duration,
        hotel_price=hotel["price"],
        transport_cost=transport["cost"]
    )

    itinerary = generate_itinerary(
        start_city=req.start_city,
        destination=req.destination,
        vibe=req.vibe,
        duration=req.duration,
        budget=req.budget,
        weather=weather
    )

    return {

        "weather": weather,

        "hotel": hotel,

        "transport": transport,

        "hotel_cost": costs["hotel_cost"],

        "food_cost": costs["food_cost"],

        "transport_cost": costs["transport_cost"],

        "estimated_cost": costs["total_cost"],

        "budget_ok": costs["total_cost"] <= req.budget,

        "itinerary": itinerary
    }