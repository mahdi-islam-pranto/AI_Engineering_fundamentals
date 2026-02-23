import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 23.777176,
    "longitude": 90.399452,
    "current_weather": True,
    "timezone": "auto"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # print all data
    print(data)

    # print current weather
    print("Current weather in Dhaka:")
    print("Temperature:", data["current_weather"]["temperature"], "°C")
    print("Wind speed:", data["current_weather"]["windspeed"], "km/h")
    print("Wind direction:", data["current_weather"]["winddirection"], "°")
else:
    print("Failed to fetch weather data. Status code:", response.status_code)
