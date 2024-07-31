from selenium import webdriver


def get_driver():
    path = r"C:\Users\user\projects\codify\bootcamp5\eshop\chromedriver\chromedriver.exe"
    cService = webdriver.ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=cService)
    driver.maximize_window()
    return driver
