from selenium.webdriver.common.by import By


class ProfilePageLocator:

    ACCOUNT_HISTORY_LOCATOR = (By.XPATH, "//a[contains(@href,'/account/order-history')]") #Кнопка История заказов
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Выход")]')  #Кнопка Выход
    PROFILE_LIST_ID_ORDERS = (By.XPATH, '//p[contains(text(),"#")]') #Список id заказов пользователя

