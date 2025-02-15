from selenium import webdriver
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture(scope="function")
def browser():
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
