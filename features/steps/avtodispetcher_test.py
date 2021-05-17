import re
import time
import logging

from behave import *

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = '/home/morglen/PycharmProjects/test_automation/res/chromedriver'


@given('Website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome(driver)
    context.browser.maximize_window()
    context.browser.get(url)


# Вставляем в строку поиска "расчет расстояний между городами"
@then("Insert text in search '{text}'")
def step(context, text):
    input = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[contains(@class, "input__control input__input mini-suggest__input")]'))
    )
    input.send_keys(text)


# Теперь нажмем на кнопку "Найти"
@then("Push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()


@then("Find href avtodispetcher '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "{}")]'.format(text)))
    )
    context.browser.find_element_by_xpath('//a[contains(@href, "{}")]'.format(text)).click()


@then("Checking URl '{text}'")
def step(context, text):
    # Запоминаем id страницы
    new_id_page = context.browser.window_handles
    # Переходим на нее
    context.browser.switch_to.window(new_id_page[1])
    # Считываем текуший URL страницы
    curr_url = context.browser.current_url
    # Проверяем его с искомым https://www.avtodispetcher.ru/distance/
    assert curr_url == text


@then("Input value from '{text}'")
def step(context, text):
    input_from = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="from"]'))
    )
    input_from.send_keys(text)


@then("Input value to '{text}'")
def step(context, text):
    input_to = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="to"]'))
    )
    input_to.send_keys(text)


@then("Set value gas '{text}'")
def step(context, text):
    input_fc = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="fc"]'))
    )
    input_fc.clear()
    input_fc.send_keys(text)


@then("Set value price on gas '{text}'")
def step(context, text):
    input_fp = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="fp"]'))
    )
    input_fp.clear()
    input_fp.send_keys(text)


@then("Click on button with value '{text}'")
def step(context, text):
    btn_input = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="{}"]'.format(text)))
    )
    btn_input.click()


@then("Checking total distance '{text}'")
def step(context, text):
    total_distance = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//span[@id="totalDistance"]'.format(text)))
    )
    assert total_distance.text == text


@then("Checking total price '{text}'")
def step(context, text):
    total_price = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "{}")]'.format(text)))
    )
    context.browser.implicitly_wait(10)
    assert re.search(text, total_price.text)


@then("Change route '{text}'")
def step(context, text):
    btn_input = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "{}")]'.format(text)))
    )
    btn_input.click()


@then("Find field between city and input city '{text}'")
def step(context, text):
    input_city = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="v"]'))
    )
    input_city.send_keys(text)


@then("Wait 30 second and click btn '{text}'")
def step(context, text):
    time.sleep(30)
    btn = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="{}"]'.format(text)))
    )
    try:
        btn.click()
    except ElementClickInterceptedException as e:
        context.browser.execute_script("arguments[0].scrollIntoView();", btn)
        btn.click()


@then("Checking new total distance '{text}'")
def step(context, text):
    total_distance = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//span[@id="totalDistance"]'))
    )
    assert total_distance.text == text


@then("Checking new total price '{text}'")
def step(context, text):
    total_price = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "{}")]'.format(text)))
    )
    context.browser.implicitly_wait(10)
    assert re.search(text, total_price.text)