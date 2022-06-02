import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.my_sportano_page import sportano_page
from Tests.Sport_Test import SportTest


class TestSportano(SportTest):

    def test_sportano(self):

        """Login with cookies confirmation"""

        sport = sportano_page(self.driver)
        sport.open_page()
        sport.nowa_nazwa()
        sport.data(self.test_data.name, self.test_data.last_name)
        sport.email_passw(self.test_data.email, self.test_data.hard_password)
        sport.check()
        sport.regist()


        assert sport.assert_account



        



















    # // *[ @ id = "my-gdpr-agreements"] / tbody / tr[1] / td / div / div / label




