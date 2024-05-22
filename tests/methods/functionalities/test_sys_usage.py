import unittest
from unittest.mock import patch, MagicMock
from src.methods.functionalities.sys_usage import system_usage


class TestSystemUsageFunction(unittest.TestCase):

    @patch('psutil.sensors_battery')
    @patch('psutil.virtual_memory')
    @patch('psutil.cpu_percent')
    @patch('src.methods.functionalities.sys_usage.speak')
    def test_system_usage(self, mock_speak, mock_cpu_percent, mock_virtual_memory, mock_sensors_battery):
        # Mock the psutil methods
        mock_cpu_percent.return_value = 50.0
        mock_virtual_memory.return_value = MagicMock(percent=70.0)
        mock_sensors_battery.return_value = MagicMock(percent=80.0)

        # Call the function
        system_usage()

        # Verify psutil methods were called
        mock_cpu_percent.assert_called_once()
        mock_virtual_memory.assert_called_once()
        mock_sensors_battery.assert_called_once()

        # Verify speak is called with the correct messages
        mock_speak.assert_any_call("CPU is at 50.0 percent")
        mock_speak.assert_any_call("Memory is at 70.0 percent")
        mock_speak.assert_any_call("Battery is at 80.0 percent")


if __name__ == '__main__':
    unittest.main()
