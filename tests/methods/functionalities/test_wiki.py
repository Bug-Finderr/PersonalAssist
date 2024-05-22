import unittest
from unittest.mock import patch

import wikipedia

from src.methods.functionalities.wiki import search_wikipedia
from src.methods.text_to_speech import speak


class TestSearchWikipediaFunction(unittest.TestCase):

    path = 'src.methods.functionalities.wiki'

    @patch(f'{path}.wikipedia.summary')
    @patch(f'{path}.speak')
    def test_search_wikipedia(self, mock_speak, mock_wikipedia_summary):
        # Mock the wikipedia.summary method
        mock_wikipedia_summary.return_value = "Python is a programming language."

        # Call the function with a search query
        search_wikipedia("Tell me about Python on Wikipedia")

        # Verify wikipedia.summary was called with the correct argument
        mock_wikipedia_summary.assert_called_once_with("tell me about python on", sentences=2)

        # Verify speak is called with the correct messages
        mock_speak.assert_any_call("Searching Wikipedia...")
        mock_speak.assert_any_call("According to Wikipedia")
        mock_speak.assert_any_call("Python is a programming language.")

    @patch(f'{path}.wikipedia.summary')
    @patch(f'{path}.speak')
    def test_search_wikipedia_no_results(self, mock_speak, mock_wikipedia_summary):
        # Mock the wikipedia.summary method to raise an exception
        mock_wikipedia_summary.side_effect = wikipedia.exceptions.PageError("Page not found.")

        # Call the function with a search query
        search_wikipedia("Tell me about nonexistent topic on Wikipedia")

        # Verify wikipedia.summary was called with the correct argument
        mock_wikipedia_summary.assert_called_once_with("tell me about nonexistent topic on", sentences=2)

        # Verify speak is called with the correct messages
        mock_speak.assert_any_call("Searching Wikipedia...")
        mock_speak.assert_any_call("Sorry, I couldn't find any information on Wikipedia.")


if __name__ == '__main__':
    unittest.main()
