import os
import subprocess
import sys


def create_install_activate():
    try:
        # Create a virtual environment named 'venv'
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("Virtual environment 'venv' created successfully.")

        # Install packages inside the virtual environment
        install_cmd = [os.path.join("venv", "Scripts", "pip"), "install",
                       "pyttsx3",
                       "datetime",
                       "SpeechRecognition",
                       "pyaudio",
                       "setuptools",
                       "pyautogui",
                       "wikipedia",
                       "pyjokes",
                       "psutil"]
        subprocess.run(["cmd.exe", "/c", ' '.join(install_cmd)], shell=True, check=True)
        print("Packages installed successfully.")

        # Activate the virtual environment
        subprocess.run(['cmd.exe', '/c', 'venv\\Scripts\\activate'], shell=True, check=True)

    except subprocess.CalledProcessError:
        print("Error creating virtual environment or installing packages.")


if __name__ == "__main__":
    create_install_activate()
