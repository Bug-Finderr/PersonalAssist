from src.methods.run_time import run_time
from src.methods.text_to_speech import speak

import datetime


@run_time
def get_time() -> None:
    cur_time: str = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {cur_time}")


@run_time
def get_date() -> None:
    cur_date: str = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"The current date is {cur_date}")
