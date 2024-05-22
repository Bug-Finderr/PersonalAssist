from src.methods.run_time import run_time
from src.methods.text_to_speech import speak
from src.methods.functionalities import date_time as dt

import datetime


@run_time
def greet() -> None:
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning, Sir.")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening, Sir.")

    dt.get_date()
    dt.get_time()
    speak("How can I help you today?")
