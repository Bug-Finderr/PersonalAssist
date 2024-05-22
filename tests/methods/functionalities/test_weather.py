import unittest
from unittest.mock import patch, MagicMock
from src.methods.functionalities.weather import get_weather


class TestGetWeatherFunction(unittest.TestCase):
    
    path = 'src.methods.functionalities.weather'

    @patch(f'{path}.speak')
    @patch(f'{path}.requests.get')
    @patch(f'{path}.config')
    def test_get_weather_success(self, mock_config, mock_get, mock_speak):
        # Mock config values
        mock_config.city = 'London'
        mock_config.weather_api = 'fake_api_key'

        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "main": {"temp": 20, "humidity": 60},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value = mock_response

        # Call the function
        get_weather()

        # Verify the API was called with the correct URL
        expected_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=fake_api_key&units=metric"
        mock_get.assert_called_once_with(expected_url)

        # Verify speak is called with the correct message
        mock_speak.assert_called_once_with("The temperature is 20°C, with clear sky, and 60% humidity")

    @patch(f'{path}.speak')
    @patch(f'{path}.requests.get')
    @patch(f'{path}.config')
    def test_get_weather_city_not_found(self, mock_config, mock_get, mock_speak):
        # Mock config values
        mock_config.city = 'InvalidCity'
        mock_config.weather_api = 'fake_api_key'

        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "404",
            "message": "city not found"
        }
        mock_get.return_value = mock_response

        # Call the function
        get_weather()

        # Verify the API was called with the correct URL
        expected_url = "https://api.openweathermap.org/data/2.5/weather?q=InvalidCity&appid=fake_api_key&units=metric"
        mock_get.assert_called_once_with(expected_url)

        # Verify speak is called with the correct message
        mock_speak.assert_called_once_with("City not found. Please try again.")


if __name__ == '__main__':
    unittest.main()
