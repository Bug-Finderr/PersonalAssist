from src.methods.run_time import run_time
from src.methods.text_to_speech import speak

import pyautogui
import config

@run_time
def take_screenshot() -> None:
    img = pyautogui.screenshot()
    img.save(config.screenshot_path)
    speak("Screenshot taken successfully!")


@run_time
def system_usage() -> None:
    import psutil

    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    battery = psutil.sensors_battery()

    speak(f"CPU usage is at {cpu_usage} percent")
    speak(f"Memory usage is at {memory.percent} percent")
    speak(f"Battery is at {battery.percent} percent")


@run_time
def increase_brightness() -> None:
    pyautogui.press("brightnessup")
    speak("Brightness increased")


@run_time
def decrease_brightness() -> None:
    pyautogui.press("brightnessdown")
    speak("Brightness decreased")


@run_time
def sleep_system() -> None:
    pyautogui.press("sleep")
    speak("System is going to sleep")


@run_time
def logout_system() -> None:
    pyautogui.press("logoff")
    speak("System is logging off")


@run_time
def shutdown_system() -> None:
    pyautogui.press("shutdown")
    speak("System is shutting down")


@run_time
def restart_system() -> None:
    pyautogui.press("restart")
    speak("System is restarting")


@run_time
def lock_system() -> None:
    pyautogui.press("lock")
    speak("System is locked")


@run_time
def mute_volume() -> None:
    pyautogui.press("volumemute")
    speak("Volume muted")


@run_time
def unmute_volume() -> None:
    pyautogui.press("volumemute")
    speak("Volume unmuted")


@run_time
def increase_volume() -> None:
    pyautogui.press("volumeup")
    speak("Volume increased")


@run_time
def decrease_volume() -> None:
    pyautogui.press("volumedown")
    speak("Volume decreased")


@run_time
def toggle_fullscreen() -> None:
    pyautogui.press("f11")
    speak("Toggled fullscreen")


@run_time
def minimize_window() -> None:
    pyautogui.hotkey("win", "down")
    speak("Window minimized")


@run_time
def maximize_window() -> None:
    pyautogui.hotkey("win", "up")
    speak("Window maximized")


@run_time
def close_window() -> None:
    pyautogui.hotkey("alt", "f4")
    speak("Window closed")


@run_time
def open_task_manager() -> None:
    pyautogui.hotkey("ctrl", "shift", "esc")
    speak("Task manager opened")


@run_time
def open_file_explorer() -> None:
    pyautogui.hotkey("win", "e")
    speak("File explorer opened")


@run_time
def open_settings() -> None:
    pyautogui.hotkey("win", "i")
    speak("Settings opened")


@run_time
def open_run_dialog() -> None:
    pyautogui.hotkey("win", "r")
    speak("Run dialog opened")