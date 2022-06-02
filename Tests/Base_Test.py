import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Tests.test_data import TestData


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.driver.implicitly_wait(20)
        self.test_data = TestData()












