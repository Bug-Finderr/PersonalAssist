import unittest
from unittest.mock import patch, MagicMock
from src.methods.text_to_speech import speak
import config


class TestSpeakFunction(unittest.TestCase):

    @patch('pyttsx3.init')
    def test_speak(self, mock_init):
        # Setup mock
        mock_engine = MagicMock()
        mock_init.return_value = mock_engine
        mock_voices = [MagicMock(id="voice0"), MagicMock(id="voice1"), MagicMock(id="voice2")]
        mock_engine.getProperty.return_value = mock_voices

        # Set the voice_id in config
        config.voice_id = 1

        # Call the function
        speak("Hello, brother")

        # Assertions
        mock_init.assert_called_once_with("sapi5")
        mock_engine.getProperty.assert_called_once_with("voices")
        mock_engine.setProperty.assert_any_call("voice", "voice1")
        mock_engine.setProperty.assert_any_call("rate", 200)
        mock_engine.say.assert_called_once_with("Hello, brother")
        mock_engine.runAndWait.assert_called_once()
        mock_engine.stop.assert_called_once()


if __name__ == '__main__':
    unittest.main()
