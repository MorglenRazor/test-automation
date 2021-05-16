from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('website "{url}"')
def step(context, url):
    # Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://yandex.ru/")


# Вставляем в строку поиска "расчет расстояний между городами"
@then("insert text in search '{text}'")
def step(context, text):
    input = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "input__control input__input mini-suggest__input")]'))
    )
    input.send_keys(text)

#Теперь нажмем на кнопку "Найти"
@then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()
