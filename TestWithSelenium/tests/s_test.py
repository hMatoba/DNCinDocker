import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

HOST = "https://webapp"

class BrowserTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor = 'http://127.0.0.1:4444/wd/hub',
            desired_capabilities = DesiredCapabilities.CHROME
        )
        self.driver.implicitly_wait(10)

    def test_404(self):
        """top page"""
        self.driver.get(HOST + "/")
        self.assertIn("NOT FOUND", self.driver.title)

def suite():
    """run tests"""
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(BrowserTests),
                    ])
    return suite


if __name__ == '__main__':
    unittest.main()
