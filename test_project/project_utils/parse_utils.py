import json


class UtilsParse:
    @staticmethod
    def parse_config():
        with open(r'..\config\config.json', 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def parse_test_data():
        with open(r'..\test_data\project_data.json', 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def parse_credentials():
        with open(r'..\credentials\credentials.json', 'r') as file:
            data = json.load(file)
            return data

