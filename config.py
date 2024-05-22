"""
Description: This file contains the configuration for the voice assistant.
"""

from dotenv import load_dotenv
import os

load_dotenv()


# Please replace the values below with your own


# Voice ID: 0 for male, 1 for female
voice_id = 1


# List of top-level domains
TLDS = ['.com', '.net', '.org', '.io', '.co', '.in']


# Path to the browser
browser_name = "brave"
browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"


# Path to music directory
music_path = "D:/Music"
music_app = "vlc.exe"


# Path to the screenshot directory
screenshot_path = "D:/ss.png"


# Openweathermap API key (Replace it here as a "string" else you're smart enough to figure out)
weather_api = os.getenv("WEATHER_API")      # Get your API key from https://openweathermap.org/api
city = "Bangalore"      # City name


# List of applications in the system
APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE",
    "outlook": "OUTLOOK.EXE",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "brave": "brave.exe",
    "edge": "msedge.exe",
    "code": "Code.exe",
    "pycharm": "pycharm64.exe",
    "sublime": "sublime_text.exe",
    "eclipse": "eclipse.exe",
    "intellij": "idea64.exe",
    "android studio": "studio64.exe",
    "unity": "Unity.exe",
    "unreal engine": "UE4Editor.exe",
    "blender": "blender.exe",
    "maya": "maya.exe",
    "docker": "Docker Desktop.exe",
    "photoshop": "photoshop.exe",
    "illustrator": "illustrator.exe",
    "after effects": "afterfx.exe",
    "premiere pro": "premiere.exe",
    "audition": "audition.exe",
    "lightroom": "lightroom.exe",
    "bridge": "bridge.exe",
    "xd": "XD.exe",
    "in design": "indesign.exe",
    "acrobat": "AcroRd32.exe",
    "microsoft teams": "Teams.exe",
    "zoom": "Zoom.exe",
    "skype": "Skype.exe",
    "telegram": "Telegram.exe",
    "whatsapp": "WhatsApp.exe",
    "discord": "Discord.exe",
    "spotify": "Spotify.exe",
    "vlc": "vlc.exe",
    "media player": "wmplayer.exe",
    "photos": "Microsoft.Photos.exe",
    "camera": "WindowsCamera.exe",
    "settings": "SystemSettings.exe",
    "control panel": "control.exe",
    "task manager": "Taskmgr.exe",
    "explorer": "explorer.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "terminal": "wt.exe",
    "python": "python.exe",
    "anaconda": "anaconda-navigator.exe",
    "jupyter": "jupyter-notebook.exe",
    "git": "git-bash.exe",
    "slack": "slack.exe",
    "trello": "Trello.exe",
    "notion": "Notion.exe",
    "obs": "obs64.exe",
}
