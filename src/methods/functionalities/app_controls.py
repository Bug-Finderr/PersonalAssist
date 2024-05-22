from src.methods.run_time import run_time
from src.methods.text_to_speech import speak
import pyautogui as gui
import os
import config

# todo: type_text, press_key, move_mouse, click_mouse, drag_mouse


@run_time
def open_app(query: str) -> None:
    app: str = [config.APPS[i] for i in config.APPS if i in query][0]

    try:
        os.startfile(app)
        speak(f"Opening {app} for you.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't open the application.")


@run_time
def close_app(query: str) -> None:
    app: str = [config.APPS[i] for i in config.APPS if i in query][0]

    try:
        os.system(f"taskkill /f /im {app}")
        speak(f"Closing {app} for you.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't close the application.")


@run_time
def scroll_mouse(clicks: int) -> None:
    try:
        gui.scroll(clicks)
        speak("Mouse scrolled successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't scroll the mouse.")
