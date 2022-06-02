from selenium.webdriver import Keys
from webdriver_manager import driver

from Lokatory.Lokatory import sportano


class sportano_page:
    def __init__(self, driver):

        self.driver = driver

        self.accept = sportano.cookies_accept_button
        self.firstname = sportano.firstname
        self.lastname = sportano.lastname
        self.email = sportano.email_address
        self.password = sportano.password
        self.checkbox = sportano.checkbox
        self.registerX = sportano.register
        self.assert_account = sportano.assert_account

    def open_page(self):
        self.driver.get("https://sportano-qa.scommerce.cloud/customer/account/create/")

    def nowa_nazwa(self):
        self.driver.find_element(*self.accept).click()

    def data(self, name, lastname):
        self.driver.find_element(*self.firstname).send_keys(name)
        self.driver.find_element(*self.lastname).send_keys(lastname)

    def email_passw(self, mail, passw):
        self.driver.find_element(*self.email).send_keys(mail)
        self.driver.find_element(*self.password).send_keys(passw)

    def check(self):
        self.driver.find_element(*self.checkbox).click()

    def regist(self):
        self.driver.find_element(*self.registerX).send_keys(Keys.ENTER)

    def account_assert(self):
        return driver.find_element(*self.assert_account).is_displayed()
























