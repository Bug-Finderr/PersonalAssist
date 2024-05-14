import pyttsx3
import run_time as rt
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import pyautogui
import psutil
import pyjokes
import os


@rt.run_time
def speak(text: str) -> None:
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()  # blocks the program execution until all currently queued commands are processed.
    engine.stop()


@rt.run_time
def greet() -> None:
    speak("Welcome back, sir!")
    date()
    time()
    speak("How can I help you today?")


@rt.run_time
def time() -> None:
    cur_time: str = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {cur_time}")


@rt.run_time
def date() -> None:
    cur_date: str = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"The current date is {cur_date}")


@rt.run_time
def search_wikipedia(query: str) -> None:
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)


@rt.run_time
def search_online() -> None:
    speak("What do you want to search for?")
    try:
        search = get_audio()
        url = f"https://www.google.com/search?q={search}"

        for tld in ['com', 'net', 'org', 'io', 'co', 'in']:
            if tld in search:
                url = search
                break

        wb.register('brave', None, wb.BackgroundBrowser("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"))
        wb.get('brave').open_new_tab(url)
        speak(f"Here is what I found for {search} on the web.")
    except Exception as e:
        speak("Sorry, I couldn't find anything on the web.")


@rt.run_time
def take_screenshot() -> None:
    img = pyautogui.screenshot()
    img.save("D:/ss.png")


@rt.run_time
def system_usage() -> None:
    cpu = psutil.cpu_percent()
    speak(f"CPU is at {cpu} percent")
    memory = psutil.virtual_memory()
    speak(f"Memory is at {memory.percent} percent")
    battery = psutil.sensors_battery().percent
    speak(f"Battery is at {battery} percent")



@rt.run_time
def get_audio() -> str:
    r: sr.Recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="en-IN")
            print(f"You said: {said}")
        except Exception as e:
            print("Exception: " + str(e))

    return said


if __name__ == "__main__":
    greet()

    while True:
        query = get_audio().lower()

        if "hello" in query:
            speak("Hello! How can I help?")

        if "date" in query:
            date()

        if "time" in query:
            time()

        if "wikipedia" in query:
            search_wikipedia(query)

        if "search online" in query:
            search_online()

        if "screenshot" in query:
            take_screenshot()
            speak("Screenshot taken successfully!")

        if "usage" in query:
            system_usage()

        if "joke" in query:
            speak(pyjokes.get_joke())

        if "sleep" in query:
            speak("System is going to sleep now")
            os.system("shutdown /h")

        if "logout" in query:
            speak("Logging out...")
            os.system("shutdown -l")

        if "restart" in query:
            speak("Restarting...")
            os.system("shutdown /r /t 1")
            
        if "shutdown" in query:
            speak("Shutting down...")
            os.system("shutdown /s /t 1")

        if "thank you" in query:
            speak("You're welcome!")

        if "bye" in query:
            speak("Goodbye!")
            quit()
