from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import locators

service_obj = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)


def set_up():
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get(locators.goopter_url)
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span').click()
    sleep(2)

    if driver.title == 'Goopter Business Portal':
        print('We are seeing the title---"Goopter Business Portal, Congrats!"')
    else:
        print("Please check your code")
        driver.close()
        driver.quit()
