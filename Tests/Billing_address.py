from Pages.My_Billing_Page import BillingAddress
from Tests.Base_Test import BaseTest

class TestBilling(BaseTest):


    """data filling - billing address"""

    def test_billing(self):
        billing_test = BillingAddress(self.driver)
        billing_test.open_page()
        billing_test.register(self.test_data.email, self.test_data.hard_password)
        billing_test.register_click()
        billing_test.address_click()
        billing_test.data(self.test_data.name, self.test_data.last_name)
        billing_test.billing_input(self.test_data.company)
        billing_test.country_sel(self)
        billing_test.address_postcode(self.test_data.address, self.test_data.apartament, self.test_data.polish_code)
        billing_test.city_name(self.test_data.city)
        billing_test.personal_data(self.test_data.phone)
        billing_test.save_address()

        assert billing_test.assert_addr




















