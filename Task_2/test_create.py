from Task_2.base_page import BasePage
from Task_2.locators import MainPageLocators, AdvertisementPageLocators
import uuid
import re

def test_creater(browser):
    page = BasePage(browser)
    page.go_to_site()

    # Создаем
    page.find_clickable_element(MainPageLocators.CREATE_BUTTON).click()
    page.find_element(MainPageLocators.CREATE_CARD)

    # Генерируем уникальные данные
    name = f"Объявление.{uuid.uuid4().hex[:6]}"
    price = "100"
    description = "description"
    url = f"https://i.ytimg.com/vi/{uuid.uuid4().hex[:6]}/hqdefault.jpg"

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
    page.find_clickable_element(locator=MainPageLocators.get_advertisements_with_name(name=name)).click()

    # Собираем данные
    advertisement_name = page.find_element(AdvertisementPageLocators.ADVERTISMENT_NAME).text
    advertisement_price = page.find_element(AdvertisementPageLocators.ADVERTISMENT_PRICE).text
    numuric_advertisement_price = re.sub(r'\D', '', advertisement_price)
    advertisement_description = page.find_element(AdvertisementPageLocators.ADVERTISMENT_DESCRIPTION).text
    advertisement_image = page.find_element(AdvertisementPageLocators.ADVERTISMENT_IMAGE).get_attribute("src")
    
    # Проверяем
    assert advertisement_name == name, "Название не совпадает"
    assert numuric_advertisement_price == price, "Цена не совпадает"
    assert advertisement_description == description, "Описание не совпадает"
    assert advertisement_image == url, "Ссылка на картинку не совпадает"