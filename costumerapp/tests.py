from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CostumerTestCase(TestCase):
    def test_signin(self):
        path = r"C:\Users\user\projects\codify\bootcamp5\eshop\chromedriver\chromedriver.exe"
        cService = webdriver.ChromeService(executable_path=path)
        driver = webdriver.Chrome(service=cService)
        driver.get("http://localhost:8000/signin/")
        sleep(3)
        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.ID, "id_password")
        
        username_element.clear()
        username_element.send_keys("admin")
        sleep(3)
        
        password_element.clear()
        password_element.send_keys("admin")
        sleep(3)
        password_element.send_keys(Keys.RETURN)
        assert "Вы успешно авторизовались!" in driver.page_source
        sleep(5)
        
        driver.close()
