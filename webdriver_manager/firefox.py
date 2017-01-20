from webdriver_manager import config
from webdriver_manager.config import Configuration
from webdriver_manager.driver import FireFoxDriver
from webdriver_manager.manager import DriverManager
from webdriver_manager import utils


class GeckoDriverManager(DriverManager):
    def __init__(self, os_type=utils.os_name()):
        DriverManager.__init__(self)
        self.driver = FireFoxDriver(os_type=os_type)

    def install(self):
        return self._file_manager.download_driver(self.driver).path