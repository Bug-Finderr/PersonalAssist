import unittest
from unittest.mock import patch, MagicMock
import speech_recognition as sr
from src.methods.speech_to_text import get_audio


class TestGetAudio(unittest.TestCase):

    @patch('speech_recognition.Microphone')
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google')
    def test_get_audio_success(self, mock_recognize_google, mock_listen, mock_microphone):
        mock_recognize_google.return_value = "Hello world"
        mock_listen.return_value = MagicMock()  # Mock audio data

        result = get_audio()
        self.assertEqual(result, "Hello world")

    @patch('speech_recognition.Microphone')
    @patch('speech_recognition.Recognizer.listen', side_effect=sr.WaitTimeoutError)
    def test_get_audio_timeout(self, mock_listen, mock_microphone):
        result = get_audio()
        self.assertEqual(result, "")

    @patch('speech_recognition.Microphone')
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google', side_effect=sr.UnknownValueError)
    def test_get_audio_unknown_value_error(self, mock_recognize_google, mock_listen, mock_microphone):
        mock_listen.return_value = MagicMock()  # Mock audio data

        result = get_audio()
        self.assertEqual(result, "")

    @patch('speech_recognition.Microphone')
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google', side_effect=sr.RequestError("test error"))
    def test_get_audio_request_error(self, mock_recognize_google, mock_listen, mock_microphone):
        mock_listen.return_value = MagicMock()  # Mock audio data

        result = get_audio()
        self.assertEqual(result, "")

    @patch('speech_recognition.Microphone')
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google', side_effect=Exception("test exception"))
    def test_get_audio_general_exception(self, mock_recognize_google, mock_listen, mock_microphone):
        mock_listen.return_value = MagicMock()  # Mock audio data

        result = get_audio()
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
