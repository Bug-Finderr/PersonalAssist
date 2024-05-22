from src.methods.run_time import run_time
from src.methods.text_to_speech import speak

import wikipedia


@run_time
def search_wikipedia(search_query: str) -> None:
    speak("Searching Wikipedia...")
    search_query = search_query.lower().replace("wikipedia", "").strip()
    try:
        results = wikipedia.summary(search_query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on Wikipedia.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Multiple results found. Here are some suggestions: {e.options[:5]}")