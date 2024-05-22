from src.methods.run_time import run_time

import speech_recognition as sr


@run_time
def get_audio() -> str:
    r = sr.Recognizer()      # Class init
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            said = r.recognize_google(audio, language="en-IN")
            print(f"You said: {said}\n")
            return said
        except sr.WaitTimeoutError:
            print("Timeout occurred. Please try again...\n")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again...\n")
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition service; {e} "
                  f"Please check your internet connection...\n")
        except Exception as e:
            print(f"Exception occurred: {e}\nPlease try again...\n")

    return ""
