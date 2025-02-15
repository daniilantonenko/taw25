from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):  
        self.driver = driver  
        self.base_url = "http://tech-avito-intern.jumpingcrab.com/"

    def find_element(self, locator, time=10):  
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator, time=15):  
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
    
    def is_hidden_element(self, locator, time=15):  
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element(locator))

    def go_to_site(self):  
        return self.driver.get(self.base_url)

    def scroll_to_smth(self, element):  
        return self.driver.execute_script("arguments[0].scrollIntoView(true);", element)  