import streamlit as st
from datetime import date
from agent.graph import trip_graph

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("✈️ AI Trip Planner")

st.caption(
    "Plan your trips using AI, live weather, attractions, hotels and budget estimation."
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.header("Trip Details")

    source = st.text_input(
        "Source",
        value="Hyderabad"
    )

    destination = st.text_input(
        "Destination",
        value="Goa"
    )

    start_date = st.date_input(
        "Start Date",
        value=date.today()
    )

    end_date = st.date_input(
        "End Date",
        value=date.today()
    )

    travellers = st.number_input(
        "Travellers",
        min_value=1,
        value=2,
    )

    hotel_rating = st.selectbox(
        "Hotel Rating",
        [3, 4, 5],
        index=1,
    )

    budget_style = st.selectbox(
        "Budget Style",
        [
            "Budget",
            "Comfort",
            "Luxury",
        ],
        index=1,
    )

    food_preference = st.selectbox(
        "Food Preference",
        [
            "Vegetarian",
            "Non Vegetarian",
            "Vegan",
        ],
    )

    transport_preference = st.selectbox(
        "Transport Preference",
        [
            "Balanced",
            "Fastest",
            "Cheapest",
        ],
    )

    st.divider()

    plan_trip = st.button(
        "🚀 Plan My Trip",
        use_container_width=True,
    )

# ----------------------------------------------------
# Main Area
# ----------------------------------------------------

if not plan_trip:

    st.info("👈 Fill in your trip details and click **Plan My Trip**.")

else:

    with st.spinner("Planning your trip..."):

        # We'll connect LangGraph here next.
        pass

    st.success("Trip planned successfully!")

    # ------------------------------------------------
    # Trip Overview
    # ------------------------------------------------

    st.header("📋 Trip Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Destination", destination)
    col2.metric("Travellers", travellers)
    col3.metric("Budget", budget_style)
    col4.metric("Hotel", f"{hotel_rating} ⭐")

    st.divider()

    # ------------------------------------------------
    # Transport
    # ------------------------------------------------

    st.header("🚆 Transport Options")

    st.info("Transport cards will appear here.")

    st.divider()

    # ------------------------------------------------
    # Hotel
    # ------------------------------------------------

    st.header("🏨 Recommended Hotel")

    st.info("Hotel information will appear here.")

    st.divider()

    # ------------------------------------------------
    # Weather
    # ------------------------------------------------

    st.header("🌤 Weather Forecast")

    st.info("Weather forecast will appear here.")

    st.divider()

    # ------------------------------------------------
    # Attractions
    # ------------------------------------------------

    st.header("📍 Attractions")

    st.info("Attractions will appear here.")

    st.divider()

    # ------------------------------------------------
    # Budget
    # ------------------------------------------------

    st.header("💰 Budget Summary")

    st.info("Budget breakdown will appear here.")

    st.divider()

    # ------------------------------------------------
    # Itinerary
    # ------------------------------------------------

    st.header("🗓 AI Itinerary")

    st.info("Generated itinerary will appear here.")

    st.divider()

    # ------------------------------------------------
    # PDF
    # ------------------------------------------------

    st.download_button(
        "⬇ Download Itinerary (PDF)",
        data=b"",
        file_name="trip.pdf",
    )