from Task_2.base_page import BasePage
from Task_2.locators import MainPageLocators, AdvertisementPageLocators
from faker import Faker
import uuid

def test_creater(browser):
    page = BasePage(browser)
    page.go_to_site()

    # Создаем
    page.find_clickable_element(MainPageLocators.CREATE_BUTTON).click()
    page.find_element(MainPageLocators.CREATE_CARD)

    # Генерируем уникальные данные
    fake = Faker('ru_RU')
    name = f"Объявление.{uuid.uuid4().hex[:6]}"
    price = "100"
    description = "description"
    url = fake.image_url()

    # Вводим данные
    page.find_element(MainPageLocators.CREATE_NAME).send_keys(name)
    page.find_element(MainPageLocators.CREATE_PRICE).send_keys(price)
    page.find_element(MainPageLocators.CREATE_DESCRIPTION).send_keys(description)    
    page.find_element(MainPageLocators.CREATE_URL_IMAGE).send_keys(url)

    # Сохраняем
    page.find_clickable_element(MainPageLocators.CREATE_BUTTON_SAVE).click()
    page.is_hidden_element(MainPageLocators.CREATE_CARD)
  
    # Переходим на страницу объявления
    page.find_element(MainPageLocators.SEARCH_INPUT).send_keys(name)
    page.find_clickable_element(MainPageLocators.ADVERTISMENT_FIRST).click()
    
    # Проверяем
    assert page.find_element(AdvertisementPageLocators.ADVERTISMENT_NAME).text == name
    assert page.find_element(AdvertisementPageLocators.ADVERTISMENT_PRICE).text == price
    assert page.find_element(AdvertisementPageLocators.ADVERTISMENT_DESCRIPTION).text == description
    assert page.find_element(AdvertisementPageLocators.ADVERTISMENT_IMAGE).get_attribute("src") == url