import streamlit as st
import streamlit.components.v1 as components
import datetime

# Page Configurations
st.set_page_config(page_title="FM Radio App", page_icon="📻", layout="centered")

# Custom CSS for 3D styling and background effects
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
        text-align: center;
        padding: 20px;
    }
    .stTitle {
        font-size: 2.5em;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
    }
    .stMarkdown {
        font-size: 1.2em;
        color: #ecf0f1;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.6);
    }
    .stSelectbox, .stButton {
        border-radius: 12px;
        box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1 class='stTitle'>📻 FM Radio App</h1>", unsafe_allow_html=True)
st.markdown("<p class='stMarkdown'>Listen to your favorite FM radio stations online.</p>", unsafe_allow_html=True)

# List of available stations with direct streaming URLs
stations = {
    "Radio 1": "https://maggie.torontocast.com:8022/stream",
    "Radio 2": "http://cast2.asurahosting.com:8569/stream",
    "Radio 3": "http://stream.zenolive.com/8ty8szwpwfeuv",
    "Radio 4": "http://stream.zeno.fm/t2ekq8zsgtzuv",
    "Radio 5": "http://e.mytuner-radio.com/embed/champion-fm-497969",
}

# Dropdown to select a station
selected_station = st.selectbox("🎵 Choose an FM station:", list(stations.keys()))

# Get the selected stream URL
stream_url = stations[selected_station]

# Display embedded audio player using HTML for better styling
st.markdown(
    f"""
    <audio controls autoplay style="box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); border-radius: 10px;">
        <source src="{stream_url}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """,
    unsafe_allow_html=True
)

st.success(f"Now playing: {selected_station}")

# Extra Feature: Display station logo or description (optional, if URLs are available)
station_images = {
    "Radio 1": "https://example.com/radio1-logo.png",
    "Radio 2": "https://example.com/radio2-logo.png",
    "Radio 3": "https://example.com/radio3-logo.png",
    "Radio 4": "https://example.com/radio4-logo.png",
    "Radio 5": "https://example.com/radio5-logo.png",
}

if selected_station in station_images:
    st.image(station_images[selected_station], caption=f"{selected_station} Logo", width=200)

# Extra Features
st.sidebar.header("📅 Current Time")
st.sidebar.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

st.sidebar.header("🔊 Volume Control")
volume = st.sidebar.slider("Set Volume", 0, 100, 50)
st.sidebar.write(f"Current Volume: {volume}%")

st.sidebar.header("📌 Favorite Stations")
fav_stations = st.sidebar.multiselect("Select Your Favorite Stations", list(stations.keys()))
if fav_stations:
    st.sidebar.write("Your Favorites:")
    for fav in fav_stations:
        st.sidebar.write(f"✅ {fav}")

# Advanced Features
st.sidebar.header("🎤 User Requests")
user_request = st.sidebar.text_area("Request a New Station")
if user_request:
    st.sidebar.write("📩 Your request has been submitted!")

st.sidebar.header("🌓 Theme Selector")
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #000000, #434343);
        }
        .stTitle, .stMarkdown {
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f5f5, #dcdcdc);
        }
        .stTitle, .stMarkdown {
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Run the app with: streamlit run app.py
