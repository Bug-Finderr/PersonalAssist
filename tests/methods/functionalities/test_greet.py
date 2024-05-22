import unittest
from unittest.mock import patch
from src.methods.functionalities.greet import greet


class TestGreetFunction(unittest.TestCase):

    @patch('src.methods.functionalities.date_time.get_time')
    @patch('src.methods.functionalities.date_time.get_date')
    @patch('src.methods.functionalities.greet.speak')
    @patch('datetime.datetime')
    def test_greet_morning(self, mock_datetime, mock_speak, mock_get_date, mock_get_time):
        # Mock the current time to morning
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 9

        # Call the function
        greet()

        # Verify speak is called with the correct greetings
        mock_speak.assert_any_call("Good Morning, Sir.")
        mock_speak.assert_any_call("How can I help you today?")
        mock_get_date.assert_called_once()
        mock_get_time.assert_called_once()

    @patch('src.methods.functionalities.date_time.get_time')
    @patch('src.methods.functionalities.date_time.get_date')
    @patch('src.methods.functionalities.greet.speak')
    @patch('datetime.datetime')
    def test_greet_afternoon(self, mock_datetime, mock_speak, mock_get_date, mock_get_time):
        # Mock the current time to afternoon
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 15

        # Call the function
        greet()

        # Verify speak is called with the correct greetings
        mock_speak.assert_any_call("Good Afternoon Sir.")
        mock_speak.assert_any_call("How can I help you today?")
        mock_get_date.assert_called_once()
        mock_get_time.assert_called_once()

    @patch('src.methods.functionalities.date_time.get_time')
    @patch('src.methods.functionalities.date_time.get_date')
    @patch('src.methods.functionalities.greet.speak')
    @patch('datetime.datetime')
    def test_greet_evening(self, mock_datetime, mock_speak, mock_get_date, mock_get_time):
        # Mock the current time to evening
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 20

        # Call the function
        greet()

        # Verify speak is called with the correct greetings
        mock_speak.assert_any_call("Good Evening, Sir.")
        mock_speak.assert_any_call("How can I help you today?")
        mock_get_date.assert_called_once()
        mock_get_time.assert_called_once()


if __name__ == '__main__':
    unittest.main()
