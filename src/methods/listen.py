from src.decorators.run_time import run_time

import speech_recognition as sr


@run_time
def get_audio() -> str:
    r: sr.Recognizer = sr.Recognizer()      # Class init
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            said: str = r.recognize_google(audio, language="en-IN")
            print(f"You said: {said}\n")
            return said
        except sr.WaitTimeoutError:
            print("Timeout occurred. Please try again...\n")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again...\n")
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition service; {e}"
                  f"Please check your internet connection...\n")
        except Exception as e:
            print(f"Exception occurred: {e}\nPlease try again...\n")

    return ""


if __name__ == '__main__':
    from tests.listen_test import test
    test()
