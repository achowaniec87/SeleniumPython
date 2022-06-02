import time

from Pages.My_Register_Page import register
from Tests.Base_Test import BaseTest


class TestRegister(BaseTest):

    """Correct user registration"""

    def test_register(self):
        my_register_page = register(self.driver)
        my_register_page.open_page()
        my_register_page.create_account(self.test_data.email, self.test_data.hard_password)


        assert my_register_page.logout_assert()



