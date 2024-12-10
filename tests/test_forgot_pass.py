from pages.forgot_password_page import ForgotPasswordPage
from data import FORGOT_PAGE_URL


class TestForgotPasswordPage:
    def test_navigate_to_forgot_page(self, driver):
        page = ForgotPasswordPage(driver)
        page.navigate_to_forgot_page()
        assert page.get_current_url() == FORGOT_PAGE_URL

    def test_enter_email(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.navigate_to_forgot_page()
        forgot_page.enter_email()
        forgot_page.click_restore_button()
        assert forgot_page.page_is_reset() is True

    def test_eye_active_after_click(self, driver):
        active_eye = ForgotPasswordPage(driver)
        active_eye.navigate(FORGOT_PAGE_URL)
        active_eye.click_restore_button()
        active_eye.click_eye_button()
        assert active_eye.check_active_eye_button() is True
























