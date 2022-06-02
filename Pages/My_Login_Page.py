from Lokatory import Lokatory


class login:

    def __init__(self,driver):
        self.driver = driver

        self.username_input = Lokatory.login.log_username
        self.password_input = Lokatory.login.log_password
        self.checkbox_click = Lokatory.login.log_checkbox_click
        self.login_click = Lokatory.login.log_login_click
        self.assert_check = Lokatory.login.log_assert
        self.log_error = Lokatory.login.log_error

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.checkbox_click).click()
        self.driver.find_element(*self.login_click).click()

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def error_log(self):
        return self.driver.find_element(*self.log_error).text

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.assert_check).is_displayed()












