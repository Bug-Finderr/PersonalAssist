import unittest
from unittest.mock import patch, call
import src.methods.functionalities.app_controls as a


class TestMusicControls(unittest.TestCase):
    
    path = 'src.methods.functionalities.app_controls'

    @patch(f'{path}.os.startfile')
    @patch(f'{path}.speak')
    @patch(f'{path}.config.APPS', {"notepad": "notepad.exe"})
    def test_open_app_success(self, mock_speak, mock_startfile):
        # Simulate successful startfile call
        mock_startfile.return_value = None
        query = "open notepad"

        # Call the function
        a.open_app(query)

        # Check if the correct methods were called
        mock_startfile.assert_called_once_with("notepad.exe")
        mock_speak.assert_called_once_with("Opening notepad.exe for you.")

    @patch(f'{path}.os.startfile', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    @patch(f'{path}.config.APPS', {"notepad": "notepad.exe"})
    def test_open_app_failure(self, mock_speak, mock_startfile):
        query = "open notepad"

        # Call the function
        a.open_app(query)

        # Check if the correct methods were called
        mock_startfile.assert_called_once_with("notepad.exe")
        mock_speak.assert_called_once_with("Sorry, I couldn't open the application.")

    @patch(f'{path}.os.system')
    @patch(f'{path}.speak')
    @patch(f'{path}.config.APPS', {"notepad": "notepad.exe"})
    def test_close_app_success(self, mock_speak, mock_system):
        # Simulate successful system call
        mock_system.return_value = 0
        query = "close notepad"

        # Call the function
        a.close_app(query)

        # Check if the correct methods were called
        mock_system.assert_called_once_with("taskkill /f /im notepad.exe")
        mock_speak.assert_called_once_with("Closing notepad.exe for you.")

    @patch(f'{path}.os.system', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    @patch(f'{path}.config.APPS', {"notepad": "notepad.exe"})
    def test_close_app_failure(self, mock_speak, mock_system):
        query = "close notepad"

        # Call the function
        a.close_app(query)

        # Check if the correct methods were called
        mock_system.assert_called_once_with("taskkill /f /im notepad.exe")
        mock_speak.assert_called_once_with("Sorry, I couldn't close the application.")

    @patch(f'{path}.gui.scroll')
    @patch(f'{path}.speak')
    def test_scroll_mouse_success(self, mock_speak, mock_scroll):
        # Simulate successful scroll
        mock_scroll.return_value = None
        clicks = 5

        # Call the function
        a.scroll_mouse(clicks)

        # Check if the correct methods were called
        mock_scroll.assert_called_once_with(clicks)
        mock_speak.assert_called_once_with("Mouse scrolled successfully.")

    @patch(f'{path}.gui.scroll', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_scroll_mouse_failure(self, mock_speak, mock_scroll):
        clicks = 5

        # Call the function
        a.scroll_mouse(clicks)

        # Check if the correct methods were called
        mock_scroll.assert_called_once_with(clicks)
        mock_speak.assert_called_once_with("Sorry, I couldn't scroll the mouse.")


if __name__ == '__main__':
    unittest.main()
