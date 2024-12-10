from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_AUTH_FIELD = (By.XPATH, "//label[contains(text(),'Email')]/ancestor::fieldset//input") #Поле Email
    PASSWORD_AUTH_FIELD = (By.XPATH, "//label[contains(text(),'Пароль')]/../input") #Поле Пароль
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") #Кнопка Войти
