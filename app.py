import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Agent", page_icon="✈️")
st.title("✈️ AI Travel Agent")
st.write("Plan your perfect trip with the help of AI! by enterering your travel preferences below.")

load_dotenv()

with st.form("planner_form"):
    city = st.text_input("Destination City")
    interests = st.text_input("Your Interests (e.g., history, food, adventure)")
    submitted = st.form_submit_button("Plan My Trip")

    if submitted:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_itinerary()
            st.subheader("Your AI-Generated Itinerary:")
            st.markdown(itinerary)
        else:
            st.warning("Please fill in all fields to generate your itinerary.")