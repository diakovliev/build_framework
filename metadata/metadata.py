import os


class ReadFile:
    """
    Read file content.
    """

    def __init__(self, filename):
        self.__filename = filename

    def filename(self):
        return self.__filename


class GetEnv:
    """
    Get environment variable.
    """

    def __init__(self, env_name):
        self.__env_name = env_name

    def env_name(self):
        return self.__env_name
