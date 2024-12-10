import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по первому заказу в ленте заказов')
    def click_first_order_in_list(self):
        self.wait_and_click_element(OrderFeedPageLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Проверка видимости попапа')
    def find_popup(self):
        return self.is_visible(OrderFeedPageLocators.ORDER_POPUP_LOCATOR)

    @allure.step('Получение текста из попапа')
    def get_text_from_order_popup(self):
        return self.get_text(OrderFeedPageLocators.ORDER_POPUP_LOCATOR)

    @allure.step('Получение списка заказов')
    def list_order_numbers(self):
        self.wait_and_find_elements(OrderFeedPageLocators.ID_ORDER_LIST)
        return self.get_text(OrderFeedPageLocators.ID_ORDER_LIST)

    @allure.step('Получение количества заказов за все время')
    def get_count_all_time(self):
        return self.get_text(OrderFeedPageLocators.ALL_TIME_COUNT_LOCATOR)

    @allure.step('Получение количества заказов за сегодня')
    def get_count_today(self):
        return self.get_text(OrderFeedPageLocators.TODAY_COUNT_LOCATOR)

    @allure.step('Получение заказа из раздела В работе')
    def get_current_order_in_work(self):
        return self.get_text(OrderFeedPageLocators.CURRENT_ORDER_LOCATOR)

















