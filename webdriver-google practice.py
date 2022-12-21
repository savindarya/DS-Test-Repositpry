from selenium import webdriver
driver=webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.implicitly_wait(30)
from time import sleep

driver.get('https://www.google.ca/')

if driver.current_url == 'https://www.google.ca/' and driver.title == 'Google':
    print(f'we are at google homepage -- {driver.current_url}')
    print(f'we are seeing title message -- "Google.ca"')
    sleep(5)
    driver.close()
else:
    print(f'we are not at google homepage')
    driver.close()
    driver.quit()