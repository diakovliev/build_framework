import os


class ReadFile:
    """
    Read file content.
    """

    def __init__(self, filename):
        self.__filename = filename

    def filename(self):
        return self.__filename

    def read(self):
        ret = ""

        if not os.path.isfile(self.__filename):
            raise Exception("No such file: %s!" % self.__filename)

        with open(self.__filename, 'r') as f:
            ret = f.read()

        return ret


class GetEnv:
    """
    Get environment variable.
    """

    def __init__(self, env_name):
        self.__env_name = env_name

    def env_name(self):
        return self.__env_name

    def read(self):
        ret = os.environ.get(self.__env_name, None)

        if ret is None:
            raise Exception("Can't find: %s environment variable!" % self.__env_name)

        return ret
