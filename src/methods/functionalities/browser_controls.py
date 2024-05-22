from src.methods.run_time import run_time
from src.methods.text_to_speech import speak
from src.methods.speech_to_text import get_audio

import pyautogui as gui
import webbrowser as wb
import config


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
def close_tab() -> None:
    try:
        gui.hotkey("ctrl", "w")
        speak("Tab closed successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't close the tab.")


@run_time
def open_tab() -> None:
    try:
        gui.hotkey("ctrl", "t")
        speak("Tab opened successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't open the tab.")


@run_time
def switch_tab() -> None:
    try:
        gui.hotkey("ctrl", "tab")
        speak("Tab switched successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't switch the tab.")
