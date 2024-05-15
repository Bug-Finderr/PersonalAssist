from src.methods.speak import speak
from src.methods.listen import get_audio
from src.decorators.run_time import run_time

import pyautogui
import wikipedia
import datetime
import webbrowser as wb
import psutil
import pyjokes
import config


@run_time
def greet() -> None:
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning, Sir.")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening, Sir.")

    date()
    time()
    speak("How can I help you today?")


@run_time
def time() -> None:
    cur_time: str = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {cur_time}")


@run_time
def date() -> None:
    cur_date: str = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"The current date is {cur_date}")


@run_time
def search_wikipedia(search_query: str) -> None:
    speak("Searching Wikipedia...")
    search_query: str = search_query.split("wikipedia", 1)[-1].strip()
    results: str = wikipedia.summary(search_query, sentences=2)
    speak("According to Wikipedia")
    speak(results)


@run_time
def search_online() -> None:
    speak("What do you want to search for?")
    try:
        search = get_audio()
        url = f"https://www.google.com/search?q={search}"

        for tld in config.TLDS:
            if tld in search:
                url = search
                break

        wb.register(config.browser_name, None, wb.BackgroundBrowser(config.browser_path))
        wb.get(config.browser_name).open_new_tab(url)
        speak(f"Here is what I found for {search} on the web.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't find anything on the web.")


@run_time
def take_screenshot() -> None:
    img = pyautogui.screenshot()
    img.save(config.screenshot_path)
    speak("Screenshot taken successfully!")


@run_time
def system_usage() -> None:
    cpu = psutil.cpu_percent()
    speak(f"CPU is at {cpu} percent")
    memory = psutil.virtual_memory()
    speak(f"Memory is at {memory.percent} percent")
    battery = psutil.sensors_battery().percent
    speak(f"Battery is at {battery} percent")


@run_time
def joke() -> None:
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    from tests.functionalities_test import test
    test()
