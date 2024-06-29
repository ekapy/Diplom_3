import allure
from pages.main_page import MainPage
from data import BASE_URL, ORDER_FEED_URL


class TestMainPage:
    @allure.title('Переход по клику на Конcтруктор')
    def test_navigate_constructor_with_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        assert main_page.get_current_url() == BASE_URL

    @allure.title('Переход по клику на Лента Заказов')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        main_page.page_is_feed()
        assert main_page.get_current_url() == ORDER_FEED_URL

    @allure.title('Клик по ингредиенту - появление модального окна')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        assert main_page.modal_ingredient_is_visible() is True
        assert 'Детали' in main_page.get_text_from_ingredient_modal()

    @allure.title('Закрытие модального окна игредиента')
    def test_close_modal_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        main_page.close_modal_ingredient()
        assert main_page.modal_ingredient_is_visible() is True

    @allure.title('Проверка счетчика ингредиента после добавления ингредиента')
    def test_check_count_ingredient_in_buns(self, driver):
        main_page = MainPage(driver)
        count_before = main_page.get_attribute_from_count()
        main_page.add_ingredient()
        count_after = main_page.get_attribute_from_count()
        assert count_before < count_after

    @allure.title('Залогиненый пользователь может создать заказ')
    def test_auth_user_create_order(self, driver, user_auth):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        main_page.add_ingredient()
        main_page.click_order_button()
        assert main_page.modal_window_is_visible() is True
        assert main_page.get_order_number() > 0







