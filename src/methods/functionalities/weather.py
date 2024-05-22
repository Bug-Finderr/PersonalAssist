from src.methods.run_time import run_time
from src.methods.text_to_speech import speak

import config
import requests


@run_time
def get_weather() -> None:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={config.city}&appid={config.weather_api}&units=metric"
    response = requests.get(url).json()
    if response["cod"] != "404":
        temperature = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        desc = response["weather"][0]["description"]
        speak(f"The temperature is {temperature}°C, with {desc}, and {humidity}% humidity")
    else:
        speak("City not found. Please try again.")
