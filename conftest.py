import pytest
import requests
from selenium import webdriver
from data import BASE_URL, CREATE_USER, DELETE_USER
from helpers import CreateUserData
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(BASE_URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def user_registration():
    user_data = CreateUserData.generation_data_for_registration()
    response = requests.post(CREATE_USER, data=user_data)
    token = str(response.json()["accessToken"])
    yield user_data, token
    requests.delete(DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def user_auth(driver, user_registration):
    login = LoginPage(driver)
    main_page = MainPage(driver)
    user = login.auth(user_registration)
    main_page.click_profile_button()
    yield user
    requests.delete(DELETE_USER, headers={'Authorization': user_registration[1]})


# def get_driver(name):
#     if name == "chrome":
#         chrome = webdriver.Chrome()
#         chrome.maximize_window()
#         chrome.get(BASE_URL)
#         return chrome
#     elif name == "firefox":
#         ff = webdriver.Firefox()
#         ff.maximize_window()
#         ff.get(BASE_URL)
#         return ff
#
#
# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     driver = get_driver(request.param)
#     driver.get(BASE_URL)
#     yield driver
#     driver.quit()





