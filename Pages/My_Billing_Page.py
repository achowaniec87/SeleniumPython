
from selenium.webdriver import Keys

from Lokatory.Lokatory import Billing_address


class BillingAddress:
    def __init__(self, driver):

        self.driver = driver

        self.username_input = Billing_address.email
        self.password_input = Billing_address.password
        self.password_click = Billing_address.password_click
        self.addresses_click = Billing_address.addresses_click
        self.edit = Billing_address.edit
        self.first_name = Billing_address.first_name
        self.last_name = Billing_address.last_name
        self.billing_company = Billing_address.billing_company
        self.select_country = Billing_address.select_country
        self.address1 = Billing_address.address_1
        self.address2 = Billing_address.address2
        self.postcode = Billing_address.postcode
        self.city = Billing_address.city
        self.phone = Billing_address.phone
        self.email = Billing_address.billing_email
        self.save = Billing_address.save_address
        self.assert_addr = Billing_address.assert_address


    def register(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def register_click(self):
        self.driver.find_element(*self.password_click).send_keys(Keys.ENTER)

    def address_click(self):
        self.driver.find_element(*self.addresses_click).click()
        self.driver.find_element(*self.edit).click()

    def data(self, firstname, lastname):
        self.driver.find_element(*self.first_name).send_keys(firstname)
        self.driver.find_element(*self.last_name).send_keys(lastname)

    def billing_input(self, company_name):
        self.driver.find_element(*self.billing_company).send_keys(company_name)

    def country_sel(self, country_name):
        self.driver.find_element(*self.select_country)

    def address_postcode(self, street_number, apartament, postcode):
        self.driver.find_element(*self.address1).send_keys(street_number)
        self.driver.find_element(*self. address2).send_keys(apartament)
        self.driver.find_element(*self.postcode).send_keys(postcode)

    def city_name(self, city_name):
        self.driver.find_element(*self.city).send_keys(city_name)

    def personal_data(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    def save_address(self):
        self.driver.find_element(*self.save).click()

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def assert_address(self):
        return self.driver.find_element(*self.assert_addr).is_displayed()


