import requests
import matplotlib.pyplot as plt
import numpy as np

api_key = "e238f399390113da08be81924d21fd5b"
cities = ["New York", "London", "Tokyo", "Mumbai", "Sydney", "Dubai", "Delhi"]
weather_data = []

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    return (data["main"]["temp"], data["main"]["humidity"], data["wind"]["speed"]) if "main" in data else (None, None, None)

for city in cities:
    temp, humidity, wind_speed = get_weather(city)
    if temp is not None:
        weather_data.append((city, temp, humidity, wind_speed))

if weather_data:
    city_names, temp, humidity, wind_speed = zip(*weather_data)
    x = np.arange(len(city_names))
    width = 0.3

    plt.figure(figsize=(12, 6))
    plt.bar(x - width, temp, width=width, label="Temperature (°C)", color='blue')
    plt.bar(x, humidity, width=width, label="Humidity (%)", color='green')
    plt.bar(x + width, wind_speed, width=width, label="Wind Speed (m/s)", color='red')

    plt.xticks(x, city_names, rotation=30)
    plt.title("Weather Data of Cities")
    plt.ylabel("Values")
    plt.legend()
    plt.show()
else:
    print("No valid weather data available.")

