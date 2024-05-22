import unittest
from unittest.mock import patch
import config
from src.methods.functionalities import music_controls as m


class TestMusicControls(unittest.TestCase):
    
    path = "src.methods.functionalities.music_controls"

    @patch(f'{path}.os.startfile')
    @patch(f'{path}.speak')
    def test_play_music_success(self, mock_speak, mock_startfile):
        # Configure the mocks
        mock_startfile.return_value = None

        # Call the function
        m.play_music()

        # Assertions
        mock_startfile.assert_called_once_with(config.music_path)
        mock_speak.assert_called_once_with("Playing music for you.")

    @patch(f'{path}.os.startfile', side_effect=Exception("File not found"))
    @patch(f'{path}.speak')
    def test_play_music_failure(self, mock_speak, mock_startfile):
        # Call the function
        m.play_music()

        # Assertions
        mock_startfile.assert_called_once_with(config.music_path)
        mock_speak.assert_any_call("Sorry, I couldn't play the music.")

    @patch(f'{path}.os.system')
    @patch(f'{path}.speak')
    def test_stop_music_success(self, mock_speak, mock_system):
        # Configure the mocks
        mock_system.return_value = 0

        # Call the function
        m.stop_music()

        # Assertions
        mock_system.assert_called_once_with(f"taskkill /f /im {config.music_app}")
        mock_speak.assert_called_once_with("Music stopped successfully.")

    @patch(f'{path}.os.system', side_effect=Exception("Taskkill failed"))
    @patch(f'{path}.speak')
    def test_stop_music_failure(self, mock_speak, mock_system):
        # Call the function
        m.stop_music()

        # Assertions
        mock_system.assert_called_once_with(f"taskkill /f /im {config.music_app}")
        mock_speak.assert_any_call("Sorry, I couldn't stop the music.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey')
    def test_next_song_success(self, mock_hotkey, mock_speak):
        m.next_song()
        mock_hotkey.assert_called_once_with("ctrl", "right")
        mock_speak.assert_called_once_with("Next song played successfully.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey')
    def test_next_song_failure(self, mock_hotkey, mock_speak):
        mock_hotkey.side_effect = Exception("Hotkey error")
        m.next_song()
        mock_hotkey.assert_called_once_with("ctrl", "right")
        mock_speak.assert_called_once_with("Sorry, I couldn't play the next song.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey')
    def test_previous_song_success(self, mock_hotkey, mock_speak):
        m.previous_song()
        mock_hotkey.assert_called_once_with("ctrl", "left")
        mock_speak.assert_called_once_with("Previous song played successfully.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey')
    def test_previous_song_failure(self, mock_hotkey, mock_speak):
        mock_hotkey.side_effect = Exception("Hotkey error")
        m.previous_song()
        mock_hotkey.assert_called_once_with("ctrl", "left")
        mock_speak.assert_called_once_with("Sorry, I couldn't play the previous song.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey')
    def test_volume_up_success(self, mock_hotkey, mock_speak):
        # Simulate a successful hotkey press
        m.volume_up()
        mock_hotkey.assert_called_once_with("ctrl", "up")
        mock_speak.assert_called_once_with("Volume increased successfully.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey', side_effect=Exception("Test exception"))
    def test_volume_up_failure(self, mock_hotkey, mock_speak):
        # Simulate an exception in hotkey press
        m.volume_up()
        mock_hotkey.assert_called_once_with("ctrl", "up")
        mock_speak.assert_called_once_with("Sorry, I couldn't increase the volume.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey')
    def test_volume_down_success(self, mock_hotkey, mock_speak):
        # Simulate a successful hotkey press
        m.volume_down()
        mock_hotkey.assert_called_once_with("ctrl", "down")
        mock_speak.assert_called_once_with("Volume decreased successfully.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.hotkey', side_effect=Exception("Test exception"))
    def test_volume_down_failure(self, mock_hotkey, mock_speak):
        # Simulate an exception in hotkey press
        m.volume_down()
        mock_hotkey.assert_called_once_with("ctrl", "down")
        mock_speak.assert_called_once_with("Sorry, I couldn't decrease the volume.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.press')
    def test_mute_volume_success(self, mock_press, mock_speak):
        mock_press.return_value = None  # Simulate successful key press
        m.mute_volume()
        mock_press.assert_called_once_with("m")
        mock_speak.assert_called_once_with("Volume muted successfully.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.press', side_effect=Exception("Key press failed"))
    def test_mute_volume_failure(self, mock_press, mock_speak):
        m.mute_volume()
        mock_press.assert_called_once_with("m")
        mock_speak.assert_called_once_with("Sorry, I couldn't mute the volume.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.press')
    def test_unmute_volume_success(self, mock_press, mock_speak):
        mock_press.return_value = None  # Simulate successful key press
        m.unmute_volume()
        mock_press.assert_called_once_with("m")
        mock_speak.assert_called_once_with("Volume unmuted successfully.")

    @patch(f'{path}.speak')
    @patch(f'{path}.gui.press', side_effect=Exception("Key press failed"))
    def test_unmute_volume_failure(self, mock_press, mock_speak):
        m.unmute_volume()
        mock_press.assert_called_once_with("m")
        mock_speak.assert_called_once_with("Sorry, I couldn't unmute the volume.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_repeat_song_success(self, mock_speak, mock_gui_press):
        # Simulate successful key press
        mock_gui_press.return_value = None

        # Call the function
        m.repeat_song()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("r")
        mock_speak.assert_called_once_with("Song repeated successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_repeat_song_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.repeat_song()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("r")
        mock_speak.assert_called_once_with("Sorry, I couldn't repeat the song.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_shuffle_songs_success(self, mock_speak, mock_gui_press):
        # Simulate successful key press
        mock_gui_press.return_value = None

        # Call the function
        m.shuffle_songs()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("s")
        mock_speak.assert_called_once_with("Songs shuffled successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_shuffle_songs_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.shuffle_songs()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("s")
        mock_speak.assert_called_once_with("Sorry, I couldn't shuffle the songs.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_play_pause_success(self, mock_speak, mock_gui_press):
        # Simulate successful key press
        mock_gui_press.return_value = None

        # Call the function
        m.play_pause()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("space")
        mock_speak.assert_called_once_with("Music played/paused successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_play_pause_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.play_pause()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("space")
        mock_speak.assert_called_once_with("Sorry, I couldn't play/pause the music.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_seek_forward_success(self, mock_speak, mock_gui_press):
        # Simulate successful key presses
        mock_gui_press.return_value = None

        # Call the function
        m.seek_forward()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("right", presses=5)
        mock_speak.assert_called_once_with("Seeked forward successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_seek_forward_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.seek_forward()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("right", presses=5)
        mock_speak.assert_called_once_with("Sorry, I couldn't seek forward.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_seek_backward_success(self, mock_speak, mock_gui_press):
        # Simulate successful key presses
        mock_gui_press.return_value = None

        # Call the function
        m.seek_backward()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("left", presses=5)
        mock_speak.assert_called_once_with("Seeked backward successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_seek_backward_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.seek_backward()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("left", presses=5)
        mock_speak.assert_called_once_with("Sorry, I couldn't seek backward.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_increase_speed_success(self, mock_speak, mock_gui_press):
        # Simulate successful key press
        mock_gui_press.return_value = None

        # Call the function
        m.increase_speed()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("plus")
        mock_speak.assert_called_once_with("Speed increased successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_increase_speed_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.increase_speed()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("plus")
        mock_speak.assert_called_once_with("Sorry, I couldn't increase the speed.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_decrease_speed_success(self, mock_speak, mock_gui_press):
        # Simulate successful key press
        mock_gui_press.return_value = None

        # Call the function
        m.decrease_speed()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("minus")
        mock_speak.assert_called_once_with("Speed decreased successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_decrease_speed_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.decrease_speed()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("minus")
        mock_speak.assert_called_once_with("Sorry, I couldn't decrease the speed.")

    @patch(f'{path}.gui.press')
    @patch(f'{path}.speak')
    def test_reset_speed_success(self, mock_speak, mock_gui_press):
        # Simulate successful key press
        mock_gui_press.return_value = None

        # Call the function
        m.reset_speed()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("0")
        mock_speak.assert_called_once_with("Speed reset successfully.")

    @patch(f'{path}.gui.press', side_effect=Exception("Mocked Exception"))
    @patch(f'{path}.speak')
    def test_reset_speed_failure(self, mock_speak, mock_gui_press):
        # Call the function
        m.reset_speed()

        # Check if the correct methods were called
        mock_gui_press.assert_called_once_with("0")
        mock_speak.assert_called_once_with("Sorry, I couldn't reset the speed.")


if __name__ == '__main__':
    unittest.main()
