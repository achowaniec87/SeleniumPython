from Pages.My_Login_Page import login
from Tests.Base_Test import BaseTest


class TestLogin(BaseTest):

    def test_log_in(self):

        """User account does not exist"""

        my_log_page = login(self.driver)
        my_log_page.open_page()
        my_log_page.log_in(self.test_data.email, self.test_data.password)

        assert "ERROR" in my_log_page.error_log()








