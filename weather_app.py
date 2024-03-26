import streamlit as st
import requests

# OpenWeatherMap API key
API_KEY = "b50baf47fda36310c860fdc0bc732a92"
BASE_URL = "http://api.openweathermap.org/data/2.5/"

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city_name):
    try:
        url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        st.error("Error fetching data. Please try again.")
        st.stop()

# Main function to run the Streamlit app
def main():
    st.title("Weather Application")
    
    # CSS styling
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            border: 2px solid #ddd;
            outline: none;
            box-shadow: none;
        }
        .stButton>button {
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .weather-container {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # User input for city name
    city_name = st.text_input("Enter city name:", "Pakistan")

    if st.button("Get Weather"):
        # Fetch weather data
        weather_data = fetch_weather_data(city_name)
        
        if weather_data["cod"] == 200:
            # Display current weather conditions
            st.markdown("<div class='weather-container'>", unsafe_allow_html=True)
            st.write("### Current Weather Conditions")
            st.write(f"City: {weather_data['name']}")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
            
            # Display additional details
            st.write("### Additional Details")
            st.write(f"Feels Like: {weather_data['main']['feels_like']}°C")
            st.write(f"Minimum Temperature: {weather_data['main']['temp_min']}°C")
            st.write(f"Maximum Temperature: {weather_data['main']['temp_max']}°C")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(f"Error: {weather_data['message']}")

if __name__ == "__main__":
    main()
