import unittest

from Tests.Billing_address import TestBilling
from Tests.GoShop import TestGoShop
from Tests.Login import TestLogin
from Tests.Register import TestRegister
from Tests.Sportano import TestSportano
from Tests.sort import TestSort

Login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
Register = unittest.TestLoader().loadTestsFromTestCase(TestRegister)
Sort = unittest.TestLoader().loadTestsFromTestCase(TestSort)
Billing_address = unittest.TestLoader().loadTestsFromTestCase(TestBilling)
Go_shop = unittest.TestLoader().loadTestsFromTestCase(TestGoShop)
Sportano = unittest.TestLoader().loadTestsFromTestCase(TestSportano)


tests_for_run = [
    Login,
    Register,
    Sort,
    Billing_address,
    Go_shop,
    Sportano
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)




