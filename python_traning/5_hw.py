from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def find_elements(link):
    driver.get(link)
    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    # # username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
    if username is None and password is None and submit is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')

find_elements("https://www.saucedemo.com/")