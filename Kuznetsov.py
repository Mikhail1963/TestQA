import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://yohoho.cc/"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, '//*[@id="search-title"]')
input1.send_keys('Leon')

button = browser.find_element(By.XPATH, '//*[@id="search"]')
button.click()

h2 = browser.find_element(By.XPATH, '//*[@id="donate"]/div')
h2 = h2.text

assert "Просмотр доступен после доната любой суммы:" == h2





time.sleep(5)
browser.quit()  # закрываем браузер после всех манипуляций
