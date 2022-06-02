import time

from Pages.my_sort_page import SortAddress
from Tests.Base_Test import BaseTest


class TestSort(BaseTest):

    """sorting products"""

    def test_sort_by_product(self):
        orders_sort = SortAddress(self.driver)
        orders_sort.open_page()
        orders_sort.register(self.test_data.email, self.test_data.hard_password)
        orders_sort.register_click()
        orders_sort.go_shop_orders()
        orders_sort.sort_open()
        orders_sort.my_sort()
        time.sleep(5)

        assert orders_sort.assert_low


















