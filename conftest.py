import pytest
import requests
from selenium import webdriver
from data import BASE_URL, CREATE_USER, DELETE_USER
from helpers import CreateUserData


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
    yield user_data
    requests.delete(DELETE_USER, headers={'Authorization': token})


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





