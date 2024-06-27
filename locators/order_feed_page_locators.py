from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FIRST_ORDER_IN_LIST = (By.XPATH, '(//a[contains(@class, "OrderHistory_link")])[1]') #Первый бургер в списке заказов
    ID_ORDER_LIST = (By.XPATH, '//p[contains(text(), "#")]') #Список id заказов
    ORDER_POPUP_LOCATOR = (By.XPATH, '//div[contains(@class,"Modal_orderBox")]') #Попап с доп информацией о заказе
    ALL_TIME_COUNT_LOCATOR = (By.XPATH, '//p[contains(text(),"Выполнено за все время:")]/following-sibling::p') #Количество заказов за все время
    TODAY_COUNT_LOCATOR = (By.XPATH, '//p[contains(text(),"Выполнено за сегодня:")]/following-sibling::p') #Количество заказов за сегодня
    CURRENT_ORDER_LOCATOR = (By.XPATH, '//*[contains(@class, "orderListReady")]//li[contains(@class, "digits-default")]') #Текущие заказы в работе

