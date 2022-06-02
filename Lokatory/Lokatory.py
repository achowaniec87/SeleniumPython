from selenium.webdriver.common.by import By



class Go_shop:

    email_adress_input = (By.ID, "reg_email")
    password_input = (By.ID, "reg_password")
    register_click = (By.NAME, "register")
    Orders_click = (By.LINK_TEXT, "Orders")
    Go_Shop_Click = (By.LINK_TEXT, "Go shop")
    Add_Cart = (By.LINK_TEXT, "Add to cart")
    View_card = (By.XPATH, "//*[@id='content']//*[@class='added_to_cart wc-forward']")



class Billing_address:

    email = (By.ID, "reg_email")
    password = (By.ID, "reg_password")
    password_click = (By.ID, "reg_password")
    addresses_click = (By.LINK_TEXT, "Addresses")
    edit = (By.LINK_TEXT, "Edit")
    first_name = (By.ID, "billing_first_name")
    last_name = (By.ID, "billing_last_name")
    billing_company = (By.ID, "billing_company")
    select_country = (By.ID, "billing_country")
    address_1 = (By.ID, "billing_address_1")
    address2 = (By.ID, "billing_address_2")
    postcode = (By.ID, "billing_postcode")
    city = (By.ID, "billing_city")
    phone = (By.ID, "billing_phone")
    billing_email = (By.ID, "billing_email")
    save_address = (By.CLASS_NAME, "button")
    assert_address = (By.XPATH, "//*[@id='page-7']//*[@class='woocommerce-Address-title title']//..")



class register_login:

    reg_email = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    reg_register_click = (By.NAME, "register")
    logout = (By.LINK_TEXT, "Logout")

class login:

    log_username = (By.ID, "username")
    log_password = (By.ID, "password")
    log_checkbox_click = (By.XPATH, "//input[@type='checkbox']")
    log_login_click = (By.NAME, "login")
    log_assert = (By.LINK_TEXT, 'Logout')
    log_error = (By.XPATH, "//ul[@class ='woocommerce-error']//li")
    
class sort_by:
    reg_email = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    password_click = (By.ID, "reg_password")
    orders = (By.LINK_TEXT, "Orders")
    go_shop = (By.LINK_TEXT, "Go shop")
    sort_order = (By.NAME, "orderby")
    popularity = (By.XPATH, "//*[@class='orderby']/option[1]")
    average_rating = (By.XPATH, "//*[@class='orderby']/option[2]")
    latest = (By.XPATH, "//*[@class='orderby']/option[3]")
    low_to_high = (By.XPATH, "//*[@class='orderby']/option[4]")
    high_to_low = (By.XPATH, "//*[@class='orderby']/option[5]")
    assert_low = (By.XPATH, "//*[@class='orderby']/option[4]")

class sportano:
    cookies_accept_button = (By.XPATH, "//*[@class='global-cookie__actions']//*[text()='Zaakceptuj wszystko']")
    cookies_accept_click = (By.XPATH, "//*[@class='global-cookie__actions']//*[text()='Zaakceptuj wszystko']")
    firstname = (By.ID, "firstname")
    lastname = (By.ID, "lastname")
    email_address = (By.ID, "email_address")
    password = (By.ID, "password")
    checkbox = (By.XPATH, "//*[@class='page-wrapper']//*[@class='gdpr-agreement-input checkbox required']//*[@class='checkbox-label']")
    register = (By.XPATH, "//*[@class='login-container__actions']//*[@type='submit']")
    assert_account = (By.XPATH, "//*[@id='account-nav']//*[text()='Moje konto']")



class cart_add:
    cookies_accept_button = (By.XPATH, "//*[@class='global-cookie__actions']//*[text()='Zaakceptuj wszystko']")
    cookies_accept_click = (By.XPATH, "//*[@class='global-cookie__actions']//*[text()='Zaakceptuj wszystko']")
    firstname = (By.ID, "firstname")
    lastname = (By.ID, "lastname")
    email_address = (By.ID, "email_address")
    password = (By.ID, "password")
    checkbox = (By.XPATH, "//*[@class='page-wrapper']//*[@class='gdpr-agreement-input checkbox required']//*[@class='checkbox-label']")
    register = (By.XPATH, "//*[@class='login-container__actions']//*[@type='submit']")
    tourism = (By.CSS_SELECTOR,("[class='icon-chevron-down--after js-button-s-level hide-picture-md']"))
    hiking_boots = (By.LINK_TEXT, "Buty turystyczne")
    filtr_list = (By.CSS_SELECTOR, ("[data-value='list']"))
    data_attribute = (By.CSS_SELECTOR, ("[data-attribute='plec'] [class='filter-options-title icon-chevron-down--after']"))
    man = (By.XPATH, "//*[@id='narrow-by-list']//*[text()='Mężczyzna']/..")
    confirm = (By.CSS_SELECTOR, ("[data-attribute='plec'] [class='button button--regular button__primary js-filter-submit']"))









