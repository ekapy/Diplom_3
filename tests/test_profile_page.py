import allure
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from data import LOGIN_PAGE_URL, ACCOUNT_ORDER_HISTORY_URL


class TestProfilePage:

    @allure.title('Проверка перехода на страницу Профиля по клику Личный кабинет с главной')
    @allure.description('Юзер авторизован')
    def test_navigate_to_profile_page_from_main_page(self, driver, user_auth):
        profile = ProfilePage(driver)
        assert profile.page_if_profile() is True

    @allure.title('Переход со страницы Профиля в раздел История заказов')
    def test_navigate_to_history_order_from_profile_t(self, driver, user_auth):
        profile = ProfilePage(driver)
        profile.click_history_button()
        assert profile.get_current_url() == ACCOUNT_ORDER_HISTORY_URL

    @allure.title('Клик по кнопке Выход - логаут')
    def test_click_logout_button(self, driver, user_auth):
        login = LoginPage(driver)
        profile = ProfilePage(driver)
        profile.click_logout_button()
        login.page_is_login()
        assert profile.get_current_url() == LOGIN_PAGE_URL




















