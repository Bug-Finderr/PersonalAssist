import pyttsx3
import run_time as rt
import datetime


@rt.run_time
def speak(text: str) -> None:
    engine.say(text)
    engine.runAndWait()             # blocks the program execution until all currently queued commands are processed.


@rt.run_time
def time() -> None:
    cur_time: str = datetime.datetime.now().strftime("%I:%M %p")
    print(f"The current time is {cur_time}")
    speak(f"The current time is {cur_time}")


@rt.run_time
def date() -> None:
    cur_date: str = datetime.datetime.now().strftime("%B %d, %Y")
    print(f"The current date is {cur_date}")
    speak(f"The current date is {cur_date}")


if __name__ == "__main__":
    engine = pyttsx3.init()
    date()
    print()
    time()
    print()
