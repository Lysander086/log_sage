import unittest
from unittest.mock import patch

from app.toggl.toggl_data_retriever import TogglDataRetriever
from app.config.configuration import Configuration

class TestTogglDataRetriever(unittest.TestCase):

    def setUp(self) -> None:
        config = Configuration()
        self.toggl_data_retriever = TogglDataRetriever(config)

    @patch('requests.get')
    def test_get_logged_time(self, mock_get):

        # Mock the response from the APIe
        mock_response = {
            'time_entries': [
                {'id': 1, 'description': 'Task 1', 'duration': 3600},
                {'id': 2, 'description': 'Task 2', 'duration': 1800},
                {'id': 3, 'description': 'Task 3', 'duration': 7200}
            ]
        }
        mock_get.return_value.json.return_value = mock_response

        # Create an instance of TogglDataRetriever
        toggl_data_retriever = TogglDataRetriever('your_api_token')

        # Call the method under test
        logged_time = toggl_data_retriever.get_logged_time()

        # Assert the expected result
        expected_result = mock_response
        self.assertEqual(logged_time, expected_result)

        # Assert that the API was called with the correct parameters
        mock_get.assert_called_once_with(
            toggl_data_retriever.url,
            auth=('1971800d4d82861d8f2c1651fea4d212', 'your_api_token')
        )


if __name__ == '__main__':
    unittest.main()
