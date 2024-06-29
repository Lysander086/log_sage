import json

import requests

from app.config.configuration import Configuration


class TogglDataRetriever:
    def __init__(self, config: Configuration, ):
        self.config = config
        self.url = 'https://api.track.toggl.com/api/v9/time_entries'
        print('init end')

    def get_logged_time(self):
        response = requests.get(self.url, auth=(
            '1971800d4d82861d8f2c1651fea4d212', 'api_token'))
        data = json.loads(response.text)
        return data
