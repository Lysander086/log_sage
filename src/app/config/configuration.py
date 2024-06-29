import os

from dotenv import load_dotenv


class Configuration:
    def __init__(self, ):
        load_dotenv()
        self.api_token = os.getenv('API_TOKEN')
