from selenium.webdriver.common.by import By
from time import sleep
import locators
from Products.set_up import set_up, driver


def log_in():
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/form/div/div[3]/div/div/div/button').click()
    sleep(5)

def live_order():
    driver.get('https://admin-dev.goopter.com/liveOrders')
    sleep(5)
    driver.find_element(By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']").click()
    sleep(10)

def tear_down():
    driver.quit()

set_up()
log_in()
live_order()
tear_down()