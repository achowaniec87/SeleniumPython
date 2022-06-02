from faker import Faker

class TestData:
    """
    Test Data generator
    """
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        if fake.boolean():
            self.gender = "female"
        else:
            self.gender = "male"
        self.name = fake.name()
        self.last_name = fake.last_name()
        self.password = fake.password()
        self.birthdate = fake.date()
        self.address = fake.street_address()
        self.city = fake.city()
        self.postal_code = fake.postalcode()
        self.polish_code = '59-540'
        self.state = fake.state()
        self.phone = fake.numerify("##########")
        self.alias = fake.word()
        self.hard_password = self.password +('A!123')
        self.company = 'Abakola'
        self.apartament = 'Apartament B'











