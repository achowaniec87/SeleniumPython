import time

from Pages.My_Go_Shop_Page import Go_shop
from Tests.Base_Test import BaseTest


class TestGoShop(BaseTest):

    """Go shopping correctly"""

    def test_shop(self):

        my_shopping = Go_shop(self.driver)
        my_shopping.open_page()
        my_shopping.shopping(self.test_data.email, self.test_data.hard_password)
        my_shopping.shopping_click()
        time.sleep(10)

        assert my_shopping.view_assert()



        # assert driver.find_element(By.CLASS_NAME, "added_to_cart wc-forward").is_displayed()









