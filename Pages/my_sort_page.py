from selenium.webdriver import Keys

from Lokatory.Lokatory import sort_by


class SortAddress:
    def __init__(self, driver):

        self.driver = driver

        self.email = sort_by.reg_email
        self.password = sort_by.reg_password
        self.password_click = sort_by.password_click

        self.orders = sort_by.orders
        self.go_shop = sort_by.go_shop

        self.order_sort = sort_by.sort_order
        self.popularity = sort_by.popularity
        self.average_rating = sort_by.average_rating
        self.latest = sort_by.latest
        self.low_high = sort_by.low_to_high
        self.high_low = sort_by.high_to_low
        self.assert_low = sort_by.assert_low


    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def register(self, username, password):
        self.driver.find_element(*self.email).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)

    def register_click(self):
        self.driver.find_element(*self.password_click).send_keys(Keys.ENTER)

    def go_shop_orders(self):
        self.driver.find_element(*self.orders).click()
        self.driver.find_element(*self.go_shop).click()

    def sort_open(self):
        self.driver.find_element(*self.order_sort).click()

    def my_sort(self):
        self.driver.find_element(*self.popularity).click()
        self.driver.find_element(*self.average_rating).click()
        self.driver.find_element(*self.latest).click()
        self.driver.find_element(*self.low_high).click()
        self.driver.find_element(*self.high_low)

    def data_assertion(self):
        return self.driver.find_element(*self.assert_low).is_displayed()













