from src.methods.speech_to_text import get_audio
from src.methods.text_to_speech import speak

import pyjokes
import os

# todo: integrate app_controls.py


if __name__ == '__main__':
    while True:
        command = get_audio().lower()

        if "wake" in command:
            from src.methods.functionalities import greet
            greet.greet()

            while True:
                query = get_audio().lower()

                if "hello" in query:
                    speak("Hello! How can I help?")

                elif "date" in query:
                    from src.methods.functionalities.date_time import get_date
                    get_date()

                elif "time" in query:
                    from src.methods.functionalities.date_time import get_time
                    get_time()

                elif "wikipedia" in query:
                    from src.methods.functionalities.wiki import search_wikipedia
                    search_wikipedia()

                elif "search online" in query:
                    from src.methods.functionalities.browser_controls import search_online
                    search_online()

                elif "close" in query and "tab" in query:
                    from src.methods.functionalities.browser_controls import close_tab
                    close_tab()

                elif "open" in query and "tab" in query:
                    from src.methods.functionalities.browser_controls import open_tab
                    open_tab()

                elif "switch" in query and "tab" in query:
                    from src.methods.functionalities.browser_controls import switch_tab
                    switch_tab()

                elif ("open" in query or "play" in query) and "music" in query:
                    from src.methods.functionalities.music_controls import play_music
                    play_music()

                elif "stop" in query and "music" in query:
                    from src.methods.functionalities.music_controls import stop_music
                    stop_music()

                elif ("next" in query or "skip" in query) and "song" in query:
                    from src.methods.functionalities.music_controls import next_song
                    next_song()

                elif "previous" in query and "song" in query:
                    from src.methods.functionalities.music_controls import previous_song
                    previous_song()

                elif "volume" in query and "up" in query:
                    from src.methods.functionalities.music_controls import volume_up
                    volume_up()

                elif "volume" in query and "down" in query:
                    from src.methods.functionalities.music_controls import volume_down
                    volume_down()

                elif "mute" in query:
                    from src.methods.functionalities.music_controls import mute_volume
                    mute_volume()

                elif "unmute" in query:
                    from src.methods.functionalities.music_controls import unmute_volume
                    unmute_volume()

                elif "repeat" in query:
                    from src.methods.functionalities.music_controls import repeat_song
                    repeat_song()

                elif "shuffle" in query:
                    from src.methods.functionalities.music_controls import shuffle_songs
                    shuffle_songs()

                elif "pause" in query or "resume" in query or "play" in query:
                    from src.methods.functionalities.music_controls import play_pause
                    play_pause()

                elif "forward" in query:
                    from src.methods.functionalities.music_controls import seek_forward
                    seek_forward()

                elif "backward" in query or "rewind" in query:
                    from src.methods.functionalities.music_controls import seek_backward
                    seek_backward()

                elif "increase" in query and "speed" in query:
                    from src.methods.functionalities.music_controls import increase_speed
                    increase_speed()

                elif ("decrease" in query or "reduce" in query) and "speed" in query:
                    from src.methods.functionalities.music_controls import decrease_speed
                    decrease_speed()

                elif "reset" in query and "speed" in query:
                    from src.methods.functionalities.music_controls import reset_speed
                    reset_speed()

                elif "screenshot" in query:
                    from src.methods.functionalities.system_controls import take_screenshot
                    take_screenshot()

                elif "usage" in query:
                    from src.methods.functionalities.system_controls import system_usage
                    system_usage()

                elif "weather" in query:
                    from src.methods.functionalities.weather import get_weather
                    get_weather()

                elif "joke" in query:
                    speak(pyjokes.get_joke())

                elif "sleep" in query:      # Test result: Works fine
                    speak("System is going to sleep now")
                    os.system("shutdown /h")

                elif "logout" in query:     # Test result: Works fine
                    speak("Logging out...")
                    os.system("shutdown -l")

                elif "restart" in query:    # Test result: Works fine
                    speak("Restarting...")
                    os.system("shutdown /r /t 1")

                elif "shutdown" in query:   # Test result: Works fine
                    speak("Shutting down...")
                    os.system("shutdown /s /t 1")

                elif "thank" in query:      # Test result: Works fine
                    speak("You're welcome!")

                elif "rest" in query:       # Test result: Works fine
                    speak("Going offline now. Wake me up when you need me.")
                    break

                elif "bye" in query:        # Test result: Works fine
                    speak("Goodbye!")
                    quit()

                elif query == "":           # Test result: Works fine
                    continue

                else:                       # Test result: Works fine
                    speak("Sorry, I didn't get that. Could you please repeat?")
