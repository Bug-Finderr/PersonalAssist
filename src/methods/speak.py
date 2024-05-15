import pyttsx3
import config


def speak(text: str) -> None:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[config.voice_id].id)
    engine.setProperty("rate", 200)
    print(f"Assistant: {text}\n")
    engine.say(text)
    engine.runAndWait()  # blocks the program execution until all currently queued commands are processed.
    engine.stop()


if __name__ == '__main__':
    from tests.speak_test import test
    test()
