from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON_LOCATOR = (By.XPATH, "//a[contains(@href,'/account')]")  # Кнопка Личный кабинет
    ORDER_BUTTON_LOCATOR = (By.XPATH, "//button[contains (text(),'Оформить заказ')]")  # Кнопка Оформить заказ
    CONSTRUCTOR_BUTTON_LOCATOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") #Кнопка Конструктор
    FEED_ORDER_BUTTON_LOCATOR = (By.XPATH, "//p[contains(text(),'Лента Заказов')]") #Кнопка Лента Заказов
    IN_WORK_TITLE_LOCATOR = (By.XPATH, "//p[contains(text(),'В работе')]") #Заголовок В работе
    COUNT_INGREDIENT_LOCATOR = (By.XPATH, '(//p[contains(@class,"counter")])[1]') #Счетчик первого ингредиента
    BASKET_AREA_LOCATOR = (By.XPATH, '//section[contains(@class,"BurgerConstructor_basket")]') #Пространство для добавления в корзину
    MODAL_ORDER_LOCATOR = (By.XPATH, '//section[contains(@class,"Modal_")]') #Модальное окно после создания заказа
    ORDER_NUMBER_IN_MODAL_WINDOW = (By.XPATH, '//h2[contains(@class,"modal__title")]') #Номер заказа в модалальном окне
    FIRST_INGREDIENT_LOCATOR = (By.XPATH, '(//ul[contains(@class,"BurgerIngredient")]/a)[1]') #Первый ингредиент булка
    MODAL_INGREDIENT_LOCATOR = (By.XPATH, '//div[contains(@class,"contentBox")]') #Модальное окно игредиента
    CLOSE_MODAL_LOCATOR = (By.CSS_SELECTOR, '[class*="Modal_modal__close"]') #Закрытие модального окна
    AUTH_BUTTON_MAIN_PAGE = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") #Кнопка Войти в аккаунт










