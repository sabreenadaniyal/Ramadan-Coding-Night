import streamlit as st
from datetime import datetime, time
from zoneinfo import ZoneInfo

# Set page configuration with icon and title
st.set_page_config(page_title="Time Zone App", page_icon="⏰", layout="centered")

# Apply custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #121212; /* Dark background */
            color: white;
        }
        h1, h2, h3, label {
            color: #00adb5; /* Teal color for headers */
        }
        .stButton button {
            background-color: #00adb5; 
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #007b7f; /* Darker teal on hover */
        }
        .stTextInput input, .stSelectbox select, .stMultiSelect div, .stTimeInput input {
            background-color: #333;
            color: white;
            border-radius: 5px;
        }
        .stAlert {
            background-color: #cccb97 !important;
            border-left: 5px solid #00adb5;
        }
    </style>
""", unsafe_allow_html=True)

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "America/Toronto",  # Corrected from "Canada/Toronto"
    "Australia/Sydney",
    "America/Los_Angeles",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("⏰ Time Zone App")

# Displaying current times in selected time zones
st.subheader("🌍 Select and View Current Times in Time Zones")

selected_timezones = st.multiselect(
    "Select timezones", 
    TIME_ZONES, 
    default=["UTC", "Asia/Karachi"]
)

for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"🕒 Current Time in **{tz}**: {current_time}")

# Time conversion between time zones
st.subheader("🛠️ Convert Time Between Timezones")

current_time = st.time_input("Select Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.now().date(), current_time).replace(tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"⏱️ Time in **{to_tz}**: {converted_time}")
