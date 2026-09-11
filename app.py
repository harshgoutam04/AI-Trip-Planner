import streamlit as st
from datetime import date
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

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

    with st.spinner("🔍 Searching transport..."):

        state = {
            "source": source,
            "destination": destination,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "travellers": travellers,
            "hotel_rating": hotel_rating,
            "budget_style": budget_style,
            "food_preference": food_preference,
            "transport_preference": transport_preference,

            "messages": [],

    "transport": None,
    "hotels": None,
    "selected_hotel": None,
    "attractions": None,
    "weather": None,
    "budget": None,
    "itinerary": None,

    "next_step": None,
    "missing": None,

            "completed": False,
        }

        result = trip_graph.invoke(state)

        st.write("Returned Keys:")
        st.write(list(result.keys()))

    st.success("Trip planned successfully!")

    # ------------------------------------------------
    # Trip Overview
    # ------------------------------------------------

    st.header("📋 Trip Overview")

    days = (end_date - start_date).days + 1

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📍 Destination", destination)

    col2.metric("🗓 Days", days)

    col3.metric("👥 Travellers", travellers)

    col4.metric(
        "💰 Budget Style",
        budget_style,
    )

    st.divider()

    # ------------------------------------------------
    # Transport
    # ------------------------------------------------

    st.header("🚆 Transport Options")

    transport = result["transport"]

    cols = st.columns(len(transport))

    for i, option in enumerate(transport):

        with cols[i]:

            st.subheader(option.mode)

            st.write(f"💰 ₹{option.estimated_price}")

            st.write(f"⏱ {option.duration}")

            st.caption(option.best_for)

            st.link_button(
                "Book",
                option.booking_link,
                use_container_width=True,
            )

    st.divider()

    # ------------------------------------------------
    # Hotel
    # ------------------------------------------------

    st.header("🏨 Recommended Hotel")

    hotel = result.get("selected_hotel")

    if hotel is None:
        hotels = result.get("hotels", [])
        if hotels:
            hotel = hotels[0]

    if hotel is None:
        st.warning("No hotel recommendations were found for this destination.")
    else:
        col1, col2 = st.columns([1, 2])

        with col1:

            st.metric(
                "Price / Night",
                f"₹{hotel.estimated_price}",
            )

            st.metric(
                "Distance",
                f"{hotel.distance/1000:.1f} km",
            )

        with col2:

            st.subheader(hotel.name)

            st.write(hotel.address)

            if hotel.website:

                st.link_button(
                    "Website",
                    hotel.website,
                )

    st.divider()

    # ------------------------------------------------
    # Weather
    # ------------------------------------------------

    st.header("🌤 Weather Forecast")

    weather = result["weather"]

    cols = st.columns(len(weather))

    for i, day in enumerate(weather):

        with cols[i]:

            st.metric(
                day.date,
                f"{day.temperature}°C",
            )

            st.caption(day.description)

            st.write(
                f"💧 {day.humidity}%"
            )

    st.divider()

    # ------------------------------------------------
    # Attractions
    # ------------------------------------------------

    st.header("📍 Attractions")

    for attraction in result["attractions"]:

        with st.expander(attraction.name):

            st.write(
                f"Category: {attraction.category}"
            )

            st.write(
                f"Distance: {attraction.distance/1000:.1f} km"
            )

            if attraction.wikipedia:

                st.link_button(
                    "Wikipedia",
                    attraction.wikipedia,
                )

    st.divider()

    # ------------------------------------------------
    # Budget
    # ------------------------------------------------

    st.header("💰 Budget Summary")

    budget = result["budget"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Transport",
            f"₹{budget.transport:,}"
        )

        st.metric(
            "Hotel",
            f"₹{budget.hotel:,}"
        )

        st.metric(
            "Food",
            f"₹{budget.food:,}"
        )

    with col2:

        st.metric(
            "Local",
            f"₹{budget.local_transport:,}"
        )

        st.metric(
            "Misc",
            f"₹{budget.miscellaneous:,}"
        )

        st.metric(
            "Grand Total",
            f"₹{budget.grand_total:,}"
        )

    st.success(
        f"Per Person: ₹{budget.per_person:,.0f}"
    )

    st.divider()

    # ------------------------------------------------
    # Itinerary
    # ------------------------------------------------

    st.header("🗓 AI Itinerary")

    st.markdown(
        result["itinerary"]
    )

    st.divider()

    # ------------------------------------------------
    # PDF
    # ------------------------------------------------

    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=A4)
    width, height = A4
    text = pdf.beginText(20 * mm, height - 25 * mm)
    text.setFont("Helvetica-Bold", 16)
    text.textLine("AI Trip Planner")
    text.setFont("Helvetica", 11)
    text.textLine(f"Destination: {destination}")
    text.textLine("")

    for line in result["itinerary"].splitlines():
        safe_line = line.encode("ascii", "replace").decode("ascii")
        while len(safe_line) > 95:
            text.textLine(safe_line[:95])
            safe_line = safe_line[95:]
        text.textLine(safe_line)
        if text.getY() < 20 * mm:
            pdf.drawText(text)
            pdf.showPage()
            text = pdf.beginText(20 * mm, height - 25 * mm)
            text.setFont("Helvetica", 11)

    pdf.drawText(text)
    pdf.save()

    st.download_button(
        "⬇ Download Itinerary (PDF)",
        data=pdf_buffer.getvalue(),
        file_name="trip.pdf",
        mime="application/pdf",
    )
