from Lokatory import Lokatory


class Go_shop:

    def __init__(self,driver):
        self.driver = driver

        self.email_adress_input = Lokatory.Go_shop.email_adress_input
        self.password_input = Lokatory.Go_shop.password_input
        self.register_click = Lokatory.Go_shop.register_click
        self.Orders = Lokatory.Go_shop.Orders_click
        self.Go_Shop = Lokatory.Go_shop.Go_Shop_Click
        self.Add_Card = Lokatory.Go_shop.Add_Cart
        self.view = Lokatory.Go_shop.View_card


    def shopping(self, email, password):

        self.driver.find_element(*self.email_adress_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

    def shopping_click(self):

        self.driver.find_element(*self.register_click).click()
        self.driver.find_element(*self.Orders).click()
        self.driver.find_element(*self.Go_Shop).click()
        self.driver.find_element(*self.Add_Card).click()


    def open_page(self):

        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def view_assert(self):
        return self.driver.find_element(*self.view).is_displayed()

