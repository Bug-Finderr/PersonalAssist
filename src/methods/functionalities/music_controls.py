from src.methods.run_time import run_time
from src.methods.text_to_speech import speak
import pyautogui as gui
import config
import os


@run_time
def play_music() -> None:
    try:
        os.startfile(config.music_path)
        speak("Playing music for you.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't play the music.")


@run_time
def stop_music() -> None:
    try:
        os.system(f"taskkill /f /im {config.music_app}")
        speak("Music stopped successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't stop the music.")


@run_time
def next_song() -> None:
    try:
        gui.hotkey("ctrl", "right")
        speak("Next song played successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't play the next song.")


@run_time
def previous_song() -> None:
    try:
        gui.hotkey("ctrl", "left")
        speak("Previous song played successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't play the previous song.")


@run_time
def volume_up() -> None:
    try:
        gui.hotkey("ctrl", "up")
        speak("Volume increased successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't increase the volume.")


@run_time
def volume_down() -> None:
    try:
        gui.hotkey("ctrl", "down")
        speak("Volume decreased successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't decrease the volume.")


@run_time
def mute_volume() -> None:
    try:
        gui.press("m")
        speak("Volume muted successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't mute the volume.")


@run_time
def unmute_volume() -> None:
    try:
        gui.press("m")
        speak("Volume unmuted successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't unmute the volume.")


@run_time
def repeat_song() -> None:
    try:
        gui.press("r")
        speak("Song repeated successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't repeat the song.")


@run_time
def shuffle_songs() -> None:
    try:
        gui.press("s")
        speak("Songs shuffled successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't shuffle the songs.")


@run_time
def play_pause() -> None:
    try:
        gui.press("space")
        speak("Music played/paused successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't play/pause the music.")


@run_time
def seek_forward() -> None:
    try:
        gui.press("right", presses=5)
        speak("Seeked forward successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't seek forward.")


@run_time
def seek_backward() -> None:
    try:
        gui.press("left", presses=5)
        speak("Seeked backward successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't seek backward.")


@run_time
def increase_speed() -> None:
    try:
        gui.press("plus")
        speak("Speed increased successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't increase the speed.")


@run_time
def decrease_speed() -> None:
    try:
        gui.press("minus")
        speak("Speed decreased successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't decrease the speed.")


@run_time
def reset_speed() -> None:
    try:
        gui.press("0")
        speak("Speed reset successfully.")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Sorry, I couldn't reset the speed.")
