from Lokatory import Lokatory



class register:

    def __init__(self,driver):
        self.driver = driver

        self.reg_email_input = Lokatory.register_login.reg_email
        self.reg_password_input = Lokatory.register_login.reg_password
        self.register_click = Lokatory.register_login.reg_register_click
        self.logout = Lokatory.register_login.logout


    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.register_click).click()

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def logout_assert(self):
        return self.driver.find_element(*self.logout).is_displayed()

