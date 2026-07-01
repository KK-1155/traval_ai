import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Myanmar AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("🇲🇲 Myanmar AI Travel Planner")
st.markdown(
    "Plan your trip using AI, weather, hotels, transport and budget analysis."
)

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.header("Trip Settings")

    start_city = st.selectbox(
        "Start City",
        [
            "Yangon",
            "Mandalay",
            "Naypyidaw",
            "Taunggyi"
        ]
    )

    vibe = st.selectbox(
        "Travel Vibe",
        [
            "Beach",
            "Nature",
            "Adventure",
            "Historical",
            "Food Tour"
        ]
    )

    budget = st.slider(
        "Budget (MMK)",
        min_value=100000,
        max_value=5000000,
        value=500000,
        step=50000
    )

# -----------------------------------
# Destination Recommendation
# -----------------------------------

st.subheader("🎯 Recommended Destinations")

if st.button("Recommend Destinations"):

    try:

        response = requests.post(
            f"{API_URL}/recommend",
            json={
                "start_city": start_city,
                "vibe": vibe,
                "budget": budget
            }
        )

        data = response.json()

        st.session_state["destinations"] = data["destinations"]

    except Exception as e:

        st.error(str(e))

# -----------------------------------
# Destination Select
# -----------------------------------

destinations = st.session_state.get(
    "destinations",
    []
)

if destinations:

    destination = st.selectbox(
        "Choose Destination",
        destinations
    )

    duration = st.selectbox(
        "Duration (Days)",
        [
            1, 2, 3, 4, 5,
            6, 7, 10, 14
        ]
    )

    if st.button("Generate AI Travel Plan"):

        with st.spinner(
            "Generating travel plan..."
        ):

            try:

                response = requests.post(
                    f"{API_URL}/generate-plan",
                    json={
                        "start_city": start_city,
                        "destination": destination,
                        "vibe": vibe,
                        "budget": budget,
                        "duration": duration
                    }
                )

                result = response.json()

                st.session_state["result"] = result

            except Exception as e:

                st.error(str(e))

# -----------------------------------
# Display Results
# -----------------------------------

result = st.session_state.get(
    "result"
)

if result:

    st.divider()

    col1, col2, col3 = st.columns(3)

    # Weather
    with col1:

        st.subheader("🌦 Weather")

        st.info(
            result["weather"]
        )

    # Hotel
    with col2:

        st.subheader("🏨 Hotel")

        hotel = result["hotel"]

        st.success(
            f"""
Name:
{hotel['name']}

Price:
{hotel['price']:,} MMK/night
"""
        )

    # Transport
    with col3:

        st.subheader("🚌 Transport")

        transport = result["transport"]

        st.success(
            f"""
Type:
{transport['type']}

Cost:
{transport['cost']:,} MMK
"""
        )

    st.divider()

    st.subheader("💰 Cost Breakdown")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Hotel Cost",
        f"{result['hotel_cost']:,}"
    )

    col2.metric(
        "Food Cost",
        f"{result['food_cost']:,}"
    )

    col3.metric(
        "Transport Cost",
        f"{result['transport_cost']:,}"
    )

    col4.metric(
        "Estimated Total",
        f"{result['estimated_cost']:,}"
    )

    st.divider()

    # Budget Check

    if result["budget_ok"]:

        st.success(
            "✅ Budget Sufficient"
        )

    else:

        st.error(
            f"""
❌ Budget မလောက်ပါ

Estimated Cost:
{result['estimated_cost']:,} MMK
"""
        )

    st.divider()

    st.subheader("🗺 AI Travel Itinerary")

    st.markdown(
        result["itinerary"]
    )

    st.divider()

    # PDF Button

    if st.button("📄 Generate PDF"):

        try:

            response = requests.post(
                f"{API_URL}/download-pdf",
                json={
                    "start_city": start_city,
                    "destination": destination,
                    "vibe": vibe,
                    "budget": budget,
                    "duration": duration
                }
            )

            data = response.json()

            st.success(
                f"PDF Generated: {data['pdf']}"
            )

        except Exception as e:

            st.error(str(e))