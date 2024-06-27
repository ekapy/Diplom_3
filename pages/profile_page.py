import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocator


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка видимости кнопки Выход на странице Профиля')
    def page_if_profile(self):
        return self.element_is_visible(ProfilePageLocator.LOGOUT_BUTTON_LOCATOR)

    @allure.step('Клик на раздел История заказов')
    def click_history_button(self):
        self.wait_and_click_element(ProfilePageLocator.ACCOUNT_HISTORY_LOCATOR)

    @allure.step('Клик по кнопке Выход')
    def click_logout_button(self):
        self.wait_and_click_element(ProfilePageLocator.LOGOUT_BUTTON_LOCATOR)

    @allure.step('Получение номера заказа из Истории заказа профиля')
    def get_order_id(self):
        self.wait_and_find_elements(ProfilePageLocator.PROFILE_LIST_ID_ORDERS)
        return self.get_text(ProfilePageLocator.PROFILE_LIST_ID_ORDERS)




