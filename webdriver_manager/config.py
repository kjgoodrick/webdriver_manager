import os

from configparser import ConfigParser

filename = 'config.ini'
folder = os.path.join(os.path.expanduser("~"), ".wdm")

_default_config = os.path.join(os.path.dirname(__file__), 'default.ini')


class Configuration(object):
    def __init__(self, file_name=filename,
                 config_folder=folder, section=None):
        self._parser = ConfigParser()
        self.config_file_path = os.path.join(config_folder, file_name)
        self.section = section

    def get(self, section, key):
        self._parser.read(_default_config)
        self._parser.read(self.config_file_path)
        return self._parser.get(section, key)

    def __getattr__(self, item):
        return self.get(self.section.upper(), item)
