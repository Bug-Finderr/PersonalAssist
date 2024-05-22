import unittest
from unittest.mock import patch
from src.methods.functionalities.date_time import get_time, get_date  # Assuming these are the paths to your functions


class TestDateTimeFunctions(unittest.TestCase):

    @patch('src.methods.functionalities.date_time.speak')
    @patch('datetime.datetime')
    def test_get_time(self, mock_datetime, mock_speak):
        # Mock the current time
        mock_now = mock_datetime.now.return_value
        mock_now.strftime.return_value = "10:30 AM"

        # Call the function
        get_time()

        # Verify speak is called with the correct time
        mock_speak.assert_called_once_with("The current time is 10:30 AM")

    @patch('src.methods.functionalities.date_time.speak')
    @patch('datetime.datetime')
    def test_get_date(self, mock_datetime, mock_speak):
        # Mock the current date
        mock_now = mock_datetime.now.return_value
        mock_now.strftime.return_value = "May 18, 2024"

        # Call the function
        get_date()

        # Verify speak is called with the correct date
        mock_speak.assert_called_once_with("The current date is May 18, 2024")


if __name__ == '__main__':
    unittest.main()
