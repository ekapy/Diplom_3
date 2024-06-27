import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке Личный Кабинет')
    def click_profile_button(self):
        self.wait_and_click_element(MainPageLocators.ACCOUNT_BUTTON_LOCATOR)

    @allure.step('клик по кнопке Конструктор')
    def click_constructor_button(self):
        self.wait_and_click_element(MainPageLocators.CONSTRUCTOR_BUTTON_LOCATOR)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed_button(self):
        self.wait_and_click_element(MainPageLocators.FEED_ORDER_BUTTON_LOCATOR)

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self):
        self.wait_and_click_element(MainPageLocators.FIRST_INGREDIENT_LOCATOR)

    @allure.step('Проверка наличия модального окна ингредиента')
    def modal_ingredient_is_visible(self):
        return self.is_visible(MainPageLocators.MODAL_INGREDIENT_LOCATOR)

    @allure.step('Получение текста из модального окна ингредиента')
    def get_text_from_ingredient_modal(self):
        return self.get_text(MainPageLocators.MODAL_INGREDIENT_LOCATOR)

    @allure.step('Закрытие модального окна игредиента')
    def close_modal_ingredient(self):
        self.wait_and_click_element(MainPageLocators.CLOSE_MODAL_LOCATOR)

    @allure.step('Ожидание заголовка В работе')
    def page_is_feed(self):
        self.wait_and_find_element(MainPageLocators.IN_WORK_TITLE_LOCATOR)

    @allure.step('Получение значения количества ингредиента')
    def get_attribute_from_count(self):
        return self.get_text(MainPageLocators.COUNT_INGREDIENT_LOCATOR)

    @allure.step('Перетаскивание(добавление) ингредиента')
    def add_ingredient(self):
        self.drag_and_drop(MainPageLocators.COUNT_INGREDIENT_LOCATOR, MainPageLocators.BASKET_AREA_LOCATOR)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_order_button(self):
        self.wait_and_click_element(MainPageLocators.ORDER_BUTTON_LOCATOR)

    @allure.step('Проверка наличия модального окна после создания заказа')
    def modal_window_is_visible(self):
        return self.is_visible(MainPageLocators.MODAL_ORDER_LOCATOR)

    def get_order_number(self):
        return int(self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL_WINDOW))

    @allure.title('Создание заказа')
    def make_order(self):
        self.add_ingredient()
        self.click_order_button()
        self.refresh()














