import json


class Configuration:
    def __init__(self, path):
        self.__data = {}
        with open(path, 'r') as f:
            self.__data = json.load(f)

    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self.__data, f)

    def __getattr__(self, item):
        return self.__data[item]
