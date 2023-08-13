import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://okta.ru/"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestMainPage1():
    @pytest.mark.regression
    def test_1(self, browser):
        browser.get(link)
        browser.maximize_window()

    @pytest.mark.smoke
    def test_2(self, browser):
        browser.get(link)
        browser.maximize_window()
        div1 = browser.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[2]/a[1]/div[4]/div")  # выбор товара (сервера)
        div1.click()
        time.sleep(3)

        input1 = browser.find_element(By.XPATH, '//*[@id="form"]/div/table/tbody/tr[5]/td[2]/label/span[2]')  # выбор товара (тип сервера)(радиокнопка)
        input1.click()
        time.sleep(3)

        input2 = browser.find_element(By.XPATH, '//*[@id="form"]/div/table/tbody/tr[80]/td/input')  # добавление товара в корзину
        input2.click()
        print('4394')
        time.sleep(3)

        alert1 = browser.switch_to.alert
        alert1.accept()
        time.sleep(30)


    @pytest.mark.smoke

    def test_3(self, browser):
        browser.get(link)
        browser.maximize_window()
        div1 = browser.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[4]/a[1]/div[4]/div")  # выбор товара (сервера)
        div1.click()
        time.sleep(3)

        input1 = browser.find_element(By.XPATH, '//*[@id="form"]/div/table/tbody/tr[5]/td[2]/label/span[2]')  # выбор товара (тип сервера)(радиокнопка)
        input1.click()
        time.sleep(3)

        input2 = browser.find_element(By.XPATH, '//*[@id="form"]/div/table/tbody/tr[80]/td/input')  # добавление товара в корзину
        input2.click()
        input3 = browser.find_element(By.XPATH, '//*[@id="form"]/div/table/tbody/tr[55]/td[2]/label/span[2]')  # добавление товара в корзину
        input3.click()
        print('3703')
        time.sleep(3)

        alert1 = browser.switch_to.alert
        alert1.accept()
        time.sleep(10)

        span1 = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/a/span/div')  # вход в корзину
        span1.click()
        time.sleep(10)
