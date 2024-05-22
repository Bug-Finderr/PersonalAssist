import unittest
from unittest.mock import patch
from src.methods.functionalities.browser_controls import search_online, close_tab, open_tab, switch_tab


class TestSearchOnlineFunction(unittest.TestCase):
    
    path = 'src.methods.functionalities.browser'

    @patch(f'{path}.wb')
    @patch(f'{path}.get_audio')
    @patch(f'{path}.speak')
    @patch(f'{path}.config')
    def test_search_online_valid_search(self, mock_config, mock_speak, mock_get_audio, mock_wb):
        # Mock config values
        mock_config.TLDS = ['.com', '.org', '.net']
        mock_config.browser_name = 'brave'
        mock_config.browser_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

        # Mock the audio input
        mock_get_audio.return_value = 'Python programming'

        # Call the function
        search_online()

        # Verify get_audio was called
        mock_get_audio.assert_called_once()

        # Verify web browser was registered and opened with the correct URL
        mock_wb.register.assert_called_once_with('brave', None, mock_wb.BackgroundBrowser('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'))
        mock_wb.get.assert_called_once_with('brave')
        mock_wb.get().open_new_tab.assert_called_once_with('https://www.google.com/search?q=Python programming')

        # Verify speak is called with the correct messages
        mock_speak.assert_any_call("What do you want to search for?")
        mock_speak.assert_any_call("Here is what I found for Python programming on the web.")

    @patch(f'{path}.wb')
    @patch(f'{path}.get_audio')
    @patch(f'{path}.speak')
    @patch(f'{path}.config')
    def test_search_online_with_tld(self, mock_config, mock_speak, mock_get_audio, mock_wb):
        # Mock config values
        mock_config.TLDS = ['.com', '.org', '.net']
        mock_config.browser_name = 'brave'
        mock_config.browser_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

        # Mock the audio input
        mock_get_audio.return_value = 'https://www.python.org'

        # Call the function
        search_online()

        # Verify get_audio was called
        mock_get_audio.assert_called_once()

        # Verify wb was registered and opened with the correct URL
        mock_wb.register.assert_called_once_with('brave', None, mock_wb.BackgroundBrowser('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'))
        mock_wb.get.assert_called_once_with('brave')
        mock_wb.get().open_new_tab.assert_called_once_with('https://www.python.org')

        # Verify speak is called with the correct messages
        mock_speak.assert_any_call("What do you want to search for?")
        mock_speak.assert_any_call("Here is what I found for https://www.python.org on the web.")

    @patch(f'{path}.wb')
    @patch(f'{path}.get_audio')
    @patch(f'{path}.speak')
    @patch(f'{path}.config')
    def test_search_online_exception(self, mock_config, mock_speak, mock_get_audio, mock_wb):
        # Mock config values
        mock_config.TLDS = ['.com', '.org', '.net']
        mock_config.browser_name = 'brave'
        mock_config.browser_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

        # Mock the audio input to raise an exception
        mock_get_audio.side_effect = Exception('Test exception')

        # Call the function
        search_online()

        # Verify get_audio was called
        mock_get_audio.assert_called_once()

        # Verify speak is called with the correct error message
        mock_speak.assert_any_call("What do you want to search for?")
        mock_speak.assert_any_call("Sorry, I couldn't find anything on the web.")

    @patch(f'{path}.gui.hotkey')
    @patch(f'{path}.speak')
    def test_close_tab_success(self, mock_speak, mock_gui_hotkey):
        # Simulate successful hotkey press
        mock_gui_hotkey.return_value = None

        # Call the function
        close_tab()

        # Check if the correct methods were called
        mock_gui_hotkey.assert_called_once_with("ctrl", "w")
        mock_speak.assert_called_once_with("Tab closed successfully.")

    @patch(f'{path}.gui.hotkey', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_close_tab_failure(self, mock_speak, mock_gui_hotkey):
        # Call the function
        close_tab()

        # Check if the correct methods were called
        mock_gui_hotkey.assert_called_once_with("ctrl", "w")
        mock_speak.assert_called_once_with("Sorry, I couldn't close the tab.")

    @patch(f'{path}.gui.hotkey')
    @patch(f'{path}.speak')
    def test_open_tab_success(self, mock_speak, mock_gui_hotkey):
        # Simulate successful key press
        mock_gui_hotkey.return_value = None

        # Call the function
        open_tab()

        # Check if the correct methods were called
        mock_gui_hotkey.assert_called_once_with("ctrl", "t")
        mock_speak.assert_called_once_with("Tab opened successfully.")

    @patch(f'{path}.gui.hotkey', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_open_tab_failure(self, mock_speak, mock_gui_hotkey):
        # Call the function
        open_tab()

        # Check if the correct methods were called
        mock_gui_hotkey.assert_called_once_with("ctrl", "t")
        mock_speak.assert_called_once_with("Sorry, I couldn't open the tab.")

    @patch(f'{path}.gui.hotkey')
    @patch(f'{path}.speak')
    def test_switch_tab_success(self, mock_speak, mock_gui_hotkey):
        # Simulate successful key press
        mock_gui_hotkey.return_value = None

        # Call the function
        switch_tab()

        # Check if the correct methods were called
        mock_gui_hotkey.assert_called_once_with("ctrl", "tab")
        mock_speak.assert_called_once_with("Tab switched successfully.")

    @patch(f'{path}.gui.hotkey', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_switch_tab_failure(self, mock_speak, mock_gui_hotkey):
        # Call the function
        switch_tab()

        # Check if the correct methods were called
        mock_gui_hotkey.assert_called_once_with("ctrl", "tab")
        mock_speak.assert_called_once_with("Sorry, I couldn't switch the tab.")


if __name__ == '__main__':
    unittest.main()
