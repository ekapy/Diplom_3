from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    FORGOT_PASSWORD_LOCATOR = (By.XPATH, "//a[contains(@href,'/forgot-password')]")
    EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[name="name"]')
    RESTORE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    EYE_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
    PASSWORD_FIELD_HIGHLIGHTER_LOCATOR = (By.CSS_SELECTOR, '.input_status_active')
