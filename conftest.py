import json
import os

import pytest

from fixture.application import Application

fixture = None

def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as f:
        target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    fixture = Application(browser=browser, base_url=web_config["baseUrl"],
                          user=web_config["user"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture(scope="session")
def user(request):
    user_config = load_config(request.config.getoption("--target"))["web"]
    user_login = {
        "user": user_config["user"],
        "password": user_config["password"]
    }
    return user_login

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")