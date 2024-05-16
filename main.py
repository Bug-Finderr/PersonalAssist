from src.methods.listen import get_audio
from src.methods.speak import speak

from src.methods import functionalities as f
import os


if __name__ == '__main__':
    f.greet()

    while True:
        query = get_audio().lower()

        if "hello" in query:
            speak("Hello! How can I help?")

        elif "date" in query:
            f.date()

        elif "time" in query:
            f.time()

        elif "wikipedia" in query:
            f.search_wikipedia(query)

        elif "search online" in query:
            f.search_online()

        elif "screenshot" in query:
            f.take_screenshot()

        elif "usage" in query:
            f.system_usage()

        elif "joke" in query:
            f.joke()

        elif "weather" in query:
            f.weather()

        elif "sleep" in query:        # Test result: Works fine
            speak("System is going to sleep now")
            os.system("shutdown /h")

        elif "logout" in query:       # Test result: Works fine
            speak("Logging out...")
            os.system("shutdown -l")

        elif "restart" in query:      # Test result: Works fine
            speak("Restarting...")
            os.system("shutdown /r /t 1")
            
        elif "shutdown" in query:     # Test result: Works fine
            speak("Shutting down...")
            os.system("shutdown /s /t 1")

        elif "thank" in query:    # Test result: Works fine
            speak("You're welcome!")

        elif "bye" in query:          # Test result: Works fine
            speak("Goodbye!")
            quit()

        else:
            speak("Sorry, I didn't get that. Could you please repeat?")
