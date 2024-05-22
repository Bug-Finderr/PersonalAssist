import unittest
from unittest.mock import patch, MagicMock
from src.methods.functionalities.system_controls import take_screenshot


class TestScreenshotFunction(unittest.TestCase):

    @patch('src.methods.functionalities.screenshot.speak')
    @patch('pyautogui.screenshot')
    @patch('src.methods.functionalities.screenshot.config')
    def test_take_screenshot(self, mock_config, mock_screenshot, mock_speak):
        # Mock the screenshot method and the save method of the image object
        mock_image = MagicMock()
        mock_screenshot.return_value = mock_image
        mock_config.screenshot_path = 'test_path/screenshot.png'

        # Call the function
        take_screenshot()

        # Verify screenshot was taken
        mock_screenshot.assert_called_once()

        # Verify the image was saved to the correct path
        mock_image.save.assert_called_once_with('test_path/screenshot.png')

        # Verify speak is called with the correct message
        mock_speak.assert_called_once_with("Screenshot taken successfully!")


if __name__ == '__main__':
    unittest.main()
