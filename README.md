# Personal Assistant Program

---

## Introduction
This is a Python-based personal assistant program designed to help users with various tasks using voice commands.

## Features
- **Voice Interaction:** Interact with the program using voice commands.
- **Time and Date:** Get the current time and date.
- **Wikipedia Search:** Search for information on Wikipedia.
- **Online Search:** Perform web searches using Google.
- **Take Screenshots:** Capture screenshots of your screen.
- **System Usage:** Check CPU, memory, and battery usage.
- **Jokes:** Have a laugh with random jokes.
- **System Actions:** Perform actions like sleep, logout, restart, and shutdown.

## Installation
1. Clone this repository to your local machine. *(Assuming you are cloning to your current working directory.)*

   ```
   git clone https://github.com/Bug-Finderr/PersonalAssist.git
   ```
3. Navigate to the project directory.

   ```
    cd PersonalAssist
    ```
5. Run `setup.py` to install the required packages and set up a virtual environment.

   ```
   python setup.py
   ```

## Usage
1. After setup, you must tweak some settings in `config.py` to effectively run the assistant.
2. Run `main.py` or the following command in your terminal:

   ```
   python main.py
   ```
4. Follow the prompts or say commands to interact with the assistant.
5. **Please look up to the code for the list of available commands until further updates.** <br>
   Example commands include:
   - "What's the time?"
   - "Search Wikipedia for Albert Einstein."
   - "Take a screenshot."
   - "Tell me a joke."
   - "Shutdown the system."

## Dependencies
- [**pyttsx3**](https://pypi.org/project/pyttsx3/) - Text-to-speech conversion library in Python.
- [**datetime**](https://docs.python.org/3/library/datetime.html) - Basic date and time types.
- [**speech_recognition**](https://pypi.org/project/SpeechRecognition/) - Library for performing speech recognition, with support for several engines and APIs, online and offline.
- [**wikipedia**](https://pypi.org/project/wikipedia/) - Wikipedia API for Python.
- [**webbrowser**](https://docs.python.org/3/library/webbrowser.html) - Convenient Web-browser controller.
- [**pyautogui**](https://pypi.org/project/PyAutoGUI/) - Cross-platform GUI automation for human beings.
- [**psutil**](https://pypi.org/project/psutil/) - Cross-platform lib for process and system monitoring in Python.
- [**pyjokes**](https://pypi.org/project/pyjokes/) - One line jokes for programmers (jokes as a service).
- [**os**](https://docs.python.org/3/library/os.html) - Miscellaneous operating system interfaces.
- [**pyaudio**](https://pypi.org/project/PyAudio/) - Python bindings for PortAudio.
- [**setuptools**](https://pypi.org/project/setuptools/) - Easily download, build, install, upgrade, and uninstall Python packages. (An alternate for distutils which is used in speech_recognition)
- [**logging**](https://docs.python.org/3/library/logging.html) - Flexible event logging system for applications.

## Note
- Ensure your microphone is properly configured for voice recognition.
- Some features may require additional setup or permissions on your system.
- For any issues or inquiries, feel free to contact the developer.
