from selenium.webdriver.common.by import By

class MainPageLocators:  
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.chakra-input")  # Поле поиска
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Найти']")  # Кнопка "Найти"

    CREATE_BUTTON = (By.XPATH, "//button[text() = 'Создать']")
    CREATE_CARD = (By.CSS_SELECTOR, ".chakra-modal__content-container")  # Карточка создания объявления
    CREATE_NAME = (By.CSS_SELECTOR, "input[name='name']")  # Поле "Название"
    CREATE_PRICE = (By.CSS_SELECTOR, "input[name='price']")  # Поле "Цена"
    CREATE_DESCRIPTION = (By.CSS_SELECTOR, "input[name='description']")  # Поле "Описание"
    CREATE_URL_IMAGE = (By.CSS_SELECTOR, "input[name='imageUrl']")  # Поле "Ссылка на картинку"

    CREATE_BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")

    BEFORE_PAGE_BUTTON = (By.XPATH, "//button[text() = 'Предыдущая']")  # Кнопка "Предыдущая"
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[text() = 'Следующая']")  # Кнопка "Следующая"

    ADVERTISMENTS = (By.XPATH, "//div[contains(@class, 'chakra-container')]//a") # Объявления

    # Объявление с названием
    def get_advertisements_with_name(name):
        return By.XPATH, f"//div[contains(@class, 'chakra-container')]//a//h4[text()='{name}']" 

class AdvertisementPageLocators:
    ADVERTISMENT_NAME = (By.CSS_SELECTOR, "header h2.chakra-heading") # Название
    ADVERTISMENT_PRICE = (By.CSS_SELECTOR, "header p.chakra-text") # Цена
    ADVERTISMENT_DESCRIPTION = (By.XPATH, "//header/following::div[1]//p") # Описание
    ADVERTISMENT_IMAGE = (By.CSS_SELECTOR, ".chakra-container img.chakra-image") # Изображение

    ADVERTISMENT_BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.chakra-container  button.chakra-button") # Кнопка "Добавить в корзину"
    ADVERTISMENT_BUTTON_EDIT = (By.XPATH, "(//div[contains(@class,'chakra-container')]//*[name()='svg'])[1]") # Кнопка "Редактировать"