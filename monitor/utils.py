import requests

API_KEY = "d01b2fb5c66456757d22ad440e6fd208"

def fetch_air_quality(city_name, lat, lon):
    # Fetch AQI
    aq_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    aq_response = requests.get(aq_url).json()
    aqi_value = aq_response['list'][0]['main']['aqi']
    aqi_map = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
    aqi_text = aqi_map.get(aqi_value, "Unknown")    

    # Fetch Temperature & Humidity
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    weather_response = requests.get(weather_url).json()
    temp = weather_response['main']['temp']
    humidity = weather_response['main']['humidity']

    return {
        "city_name": city_name,
        "aqi_value": aqi_value,
        "aqi_text": aqi_text,
        "temperature": temp,
        "humidity": humidity
    }
