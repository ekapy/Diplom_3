from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    def wait_and_find_element(self, locator):
        try:
            WebDriverWait(self.driver,30).until(EC.presence_of_element_located(locator))
            return self.driver.find_element(*locator)
        except TimeoutException:
            print(f'{locator} не найден')

    def wait_and_find_elements(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locator))

    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locator))
        self.wait_and_find_element(locator).click()

    def enter_text(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait_and_find_element(locator).text

    def element_is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            print(f'{locator} не найден')

    def is_not_visible(self, locator):
        try:
            WebDriverWait(self.driver,1).until(EC.invisibility_of_element(locator))
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def drag_and_drop(self, locator1, locator2):
        actions = ActionChains(self.driver)
        ingredient = self.wait_and_find_element(locator1)
        basket = self.wait_and_find_element(locator2)
        actions.drag_and_drop(ingredient, basket).perform()


























