import pytest
from base_page import BasePage
from locators import MainPageLocators, AdvertisementPageLocators
import uuid
import re
import time

@pytest.fixture(scope="module")
def create_ad(request):
    """Фикстура объявления"""
  
    # Генерируем уникальные данные
    name = f"Объявление.{uuid.uuid4().hex[:6]}"
    price = "100"
    description = "description"
    url_image = f"https://i.ytimg.com/vi/{uuid.uuid4().hex[:6]}/hqdefault.jpg"

    return name, price, description, url_image

def test_create(browser, create_ad):
    """Тест на создание объявления """
    name, price, description, url_image = create_ad
    page = BasePage(browser)
    page.go_to_site()  

    # Создаем
    page.find_clickable_element(MainPageLocators.CREATE_BUTTON).click()
    page.find_element(MainPageLocators.CREATE_CARD)

    # Вводим данные
    page.find_element(MainPageLocators.CREATE_NAME).send_keys(name)
    page.find_element(MainPageLocators.CREATE_PRICE).send_keys(price)
    page.find_element(MainPageLocators.CREATE_DESCRIPTION).send_keys(description)    
    page.find_element(MainPageLocators.CREATE_URL_IMAGE).send_keys(url_image)

    # Сохраняем
    page.find_clickable_element(MainPageLocators.CREATE_BUTTON_SAVE).click()
    page.is_hidden_element(MainPageLocators.CREATE_CARD)

    # Ищем созданное объявление
    page.find_element(MainPageLocators.SEARCH_INPUT).send_keys(name)
    advertisement = page.find_clickable_element(locator=MainPageLocators.get_advertisements_with_name(name=name))
    # Проверяем наличие объявления в поиске
    assert advertisement is not None, "Объявление не найдено"
    
    # Переходим на страницу объявления
    advertisement.click()

    # Собираем данные
    advertisement_name = page.find_element(AdvertisementPageLocators.ADVERTISMENT_NAME).text
    advertisement_price = page.find_element(AdvertisementPageLocators.ADVERTISMENT_PRICE).text
    numuric_advertisement_price = re.sub(r'\D', '', advertisement_price)
    advertisement_description = page.find_element(AdvertisementPageLocators.ADVERTISMENT_DESCRIPTION).text
    advertisement_image = page.find_element(AdvertisementPageLocators.ADVERTISMENT_IMAGE).get_attribute("src")
    
    # Проверяем соответствие данных
    assert advertisement_name == name, "Название не совпадает"
    assert numuric_advertisement_price == price, "Цена не совпадает"
    assert advertisement_description == description, "Описание не совпадает"
    assert advertisement_image == url_image, "Ссылка на картинку не совпадает"

def test_search(browser, create_ad):
    name, price, description, url_image = create_ad
    page = BasePage(browser)
    page.go_to_site()

    # Ищем созданное объявление
    page.find_element(MainPageLocators.SEARCH_INPUT).send_keys(name)
    advertisement = page.find_clickable_element(locator=MainPageLocators.get_advertisements_with_name(name=name))
    # Проверяем наличие объявления в поиске
    assert advertisement is not None, "Объявление не найдено"


def test_edit(browser, create_ad):
    name, price, description, url_image = create_ad
    page = BasePage(browser)
    page.go_to_site()

    # Ищем созданное объявление
    page.find_element(MainPageLocators.SEARCH_INPUT).send_keys(name)
    advertisement = page.find_clickable_element(locator=MainPageLocators.get_advertisements_with_name(name=name))
    # Проверяем наличие объявления в поиске
    assert advertisement is not None, "Объявление не найдено"

    # Переходим на страницу объявления
    advertisement.click()

    # Редактируем объявление
    page.find_clickable_element(AdvertisementPageLocators.ADVERTISMENT_BUTTON_EDIT).click()

    name_new = f"Объявление.{uuid.uuid4().hex[:6]}"
    price_new = "200"
    description_new = "description_new"
    url_image_new = f"https://i.ytimg.com/vi/{uuid.uuid4().hex[:6]}/hqdefault.jpg"

    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_NAME).clear()
    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_PRICE).clear()
    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_DESCRIPTION).clear()
    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_URL_IMAGE).clear()

    time.sleep(10)

    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_NAME).send_keys(name_new)
    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_PRICE).send_keys(price_new)
    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_DESCRIPTION).send_keys(description_new)
    page.find_element(AdvertisementPageLocators.ADVERTISMENT_EDIT_URL_IMAGE).send_keys(url_image_new)

    time.sleep(10)

    # Сохраняем
    page.find_clickable_element(AdvertisementPageLocators.ADVERTISMENT_BUTTON_EDIT).click()

    # Собираем данные
    advertisement_name = page.find_element(AdvertisementPageLocators.ADVERTISMENT_NAME).text
    advertisement_price = page.find_element(AdvertisementPageLocators.ADVERTISMENT_PRICE).text
    numuric_advertisement_price = re.sub(r'\D', '', advertisement_price)
    advertisement_description = page.find_element(AdvertisementPageLocators.ADVERTISMENT_DESCRIPTION).text
    advertisement_image = page.find_element(AdvertisementPageLocators.ADVERTISMENT_IMAGE).get_attribute("src")

    time.sleep(10)
    
    # Проверяем соответствие данных
    assert advertisement_name == name_new, "Название не совпадает"
    assert numuric_advertisement_price == price_new, "Цена не совпадает"
    assert advertisement_description == description_new, "Описание не совпадает"
    assert advertisement_image == url_image_new, "Ссылка на картинку не совпадает"