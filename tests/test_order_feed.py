import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from data import ORDER_FEED_URL


class TestOrderFeed():
    @allure.title('Проверка всплывающего окна при клике на заказ')
    def test_get_popup_after_order_click(self, driver):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.click_order_feed_button()
        order_page.click_first_order_in_list()
        assert order_page.find_popup() is True
        assert 'Cостав' in order_page.get_text_from_order_popup()

    @allure.title('Заказы пользователя из раздела История заказов отображаются на странице Лента заказов')
    def test_order_number_in_order_list(self, driver, user_auth):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.click_constructor_button()
        main_page.make_order()
        main_page.click_profile_button()
        profile_page.click_history_button()
        order_id = profile_page.get_order_id()
        main_page.click_order_feed_button()
        assert order_id in order_feed.list_order_numbers()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_count_order_for_all_time(self, driver, user_auth):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.click_order_feed_button()
        all_time_before = int(order_page.get_count_all_time())
        main_page.click_constructor_button()
        main_page.make_order()
        main_page.navigate(ORDER_FEED_URL)
        all_time_after = int(order_page.get_count_all_time())
        assert all_time_before < all_time_after

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_count_order_for_all_time(self, driver, user_auth):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.click_order_feed_button()
        today_count_before = int(order_page.get_count_today())
        main_page.click_constructor_button()
        main_page.make_order()
        main_page.navigate(ORDER_FEED_URL)
        today_count_after = int(order_page.get_count_today())
        assert today_count_before < today_count_after

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_check_current_order_in_work(self, driver, user_auth):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.click_constructor_button()
        main_page.make_order()
        main_page.click_profile_button()
        profile_page.click_history_button()
        order_id = profile_page.get_order_id()
        main_page.click_order_feed_button()
        main_page.click_order_feed_button()
        in_work = order_feed.get_current_order_in_work()
        assert f'#{in_work}' == order_id
























