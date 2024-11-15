import streamlit as st
import requests

# NASA API endpoint and API key
api_url = "https://api.nasa.gov/planetary/apod"
api_key = "OU8GYKj4DXd7lyOrgYkEEKREb1bZx9UffYfWaVS7"

# Fetch the daily image from NASA API
response = requests.get(api_url, params={"api_key": api_key})
data = response.json()

# Display the image and its details on the Streamlit web page
st.title("NASA Image of the Day")
if response.status_code == 200:
    st.image(data["url"], caption=data["title"])
    st.write(data["explanation"])
else:
    st.error("Failed to fetch the image from NASA API.")