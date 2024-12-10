import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.forgot_password_locators import ForgotPasswordPageLocators
from data import email


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу Восстановления пароля')
    def navigate_to_forgot_page(self):
        self.wait_and_click_element(MainPageLocators.ACCOUNT_BUTTON_LOCATOR)
        self.wait_and_click_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_LOCATOR)

    @allure.step('Ввод в поле Email')
    def enter_email(self):
        self.wait_and_find_element(ForgotPasswordPageLocators.EMAIL_FIELD_LOCATOR)
        self.enter_text(ForgotPasswordPageLocators.EMAIL_FIELD_LOCATOR, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_restore_button(self):
        self.wait_and_click_element(ForgotPasswordPageLocators.RESTORE_BUTTON_LOCATOR)

    @allure.step('Проверка перехода на страницу /reset по наличию "глазика"')
    def page_is_reset(self):
        return self.element_is_visible(ForgotPasswordPageLocators.EYE_BUTTON_LOCATOR)

    @allure.step(f'Клик по "глазику" в поле Пароль')
    def click_eye_button(self):
        self.wait_and_click_element(ForgotPasswordPageLocators.EYE_BUTTON_LOCATOR)

    @allure.step('Проверка активности поля Пароль')
    def check_active_eye_button(self):
        return self.element_is_visible(ForgotPasswordPageLocators.PASSWORD_FIELD_HIGHLIGHTER_LOCATOR)

