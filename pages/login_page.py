import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import LOGIN_PAGE_URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def auth(self, user_registration):
        self.navigate(LOGIN_PAGE_URL)
        email_data = user_registration[0]["email"]
        password_data = user_registration[0]["password"]
        self.enter_text(LoginPageLocators.EMAIL_AUTH_FIELD, email_data)
        self.enter_text(LoginPageLocators.PASSWORD_AUTH_FIELD, password_data)
        self.wait_and_click_element(LoginPageLocators.SIGN_IN_BUTTON)
        return email_data, password_data

    @allure.step('Ожидание кнопки Войти - проверка, что страница Авторизации')
    def page_is_login(self):
        self.wait_and_find_element(LoginPageLocators.SIGN_IN_BUTTON)





