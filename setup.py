import subprocess
import sys


def create_venv():
    try:
        # Create a virtual environment named 'venv'
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("Virtual environment 'venv' created successfully.")
    except subprocess.CalledProcessError:
        print("Error creating virtual environment.")
        return


def install_packages():
    try:
        # Activate the virtual environment
        subprocess.run(["venv\\Scripts\\activate"], shell=True, check=True)
        print("Virtual environment activated.")

        # Install required packages
        subprocess.run(["pip", "install", "pyttsx3", "datetime", "SpeechRecognition", "pyaudio", "setuptools",
                        "pyautogui", "wikipedia", "pyjokes", "psutil"], check=True)
        print("Packages installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing packages.")
        return


if __name__ == "__main__":
    create_venv()
    install_packages()
