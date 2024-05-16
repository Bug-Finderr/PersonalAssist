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
TLDS = ['com', 'net', 'org', 'io', 'co', 'in']

# Path to the browser
browser_name = "brave"
browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# Path to the screenshot directory
screenshot_path = "D:/ss.png"

# Openweathermap API key (Replace it here as a "string" else you're smart enough to figure out)
weather_api = os.getenv("WEATHER_API")      # Get your API key from https://openweathermap.org/api

# City name
city = "Bangalore"
