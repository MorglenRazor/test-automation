import logging
import re
import time

from behave import *

from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


@given('Website "{url}"')
def step(context, url):
    logging.info('Start Testing ...')
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
    logging.info('We insert into the search "calculation of distances between cities"')


# Теперь нажмем на кнопку "Найти"
@then("Push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()
    logging.info('Now click on the "Find" button')


# Ищем на странице поиска искомый сайт
@then("Find href avtodispetcher '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "{}")]'.format(text)))
    )
    context.browser.find_element_by_xpath('//a[contains(@href, "{}")]'.format(text)).click()
    logging.info('We are looking for the desired site on the search page')


# Проверяем правильность искомого сайта, сверя URL который мы знаем с тем на который зашли
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
    logging.info('We check the correctness of the desired site, checking the URL that we know with the one we visitedr')


# Вставляем значения "Откуда"
@then("Input value from '{text}'")
def step(context, text):
    input_from = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="from"]'))
    )
    input_from.send_keys(text)
    logging.info('Insert "From" values')


# Вставляем значение "Куда"
@then("Input value to '{text}'")
def step(context, text):
    input_to = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="to"]'))
    )
    input_to.send_keys(text)
    logging.info('Insert the value "Where"')


# Устанавливаем значения "Расход топлива"
@then("Set value gas '{text}'")
def step(context, text):
    input_fc = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="fc"]'))
    )
    input_fc.clear()
    input_fc.send_keys(text)
    logging.info('Set the "Fuel Consumption" values')


# Устанавливаем значение "Цену за литр"
@then("Set value price on gas '{text}'")
def step(context, text):
    input_fp = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="fp"]'))
    )
    input_fp.clear()
    input_fp.send_keys(text)
    logging.info('Set the value "Price per liter"')


# Нажимаем на кнопку "Рассчитать"
@then("Click on button with value '{text}'")
def step(context, text):
    btn_input = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="{}"]'.format(text)))
    )
    btn_input.click()
    logging.info('Click on the "Calculate" button')


# Проверяем дистанцию с известной
@then("Checking total distance '{text}'")
def step(context, text):
    total_distance = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//span[@id="totalDistance"]'.format(text)))
    )
    assert total_distance.text == text
    logging.info('Checking the total distancer')


# Проверяем цену с известной
@then("Checking total price '{text}'")
def step(context, text):
    total_price = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "{}")]'.format(text)))
    )
    context.browser.implicitly_wait(10)
    assert re.search(text, total_price.text)
    logging.info('Checking total price')


# Нажиммаем кнопку "Изменить маршрут"
@then("Change route '{text}'")
def step(context, text):
    btn_input = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "{}")]'.format(text)))
    )
    btn_input.click()
    logging.info('Press the button "Change route"')


# Находим поле "Между городов" и Вставляем город "Великий Новгород"
@then("Find field between city and input city '{text}'")
def step(context, text):
    input_city = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="v"]'))
    )
    input_city.send_keys(text)
    logging.info('Find the field "Between cities" and Insert the city "Veliky Novgorod"')


# Ждем 30 секунд и нажимаем на кнопку "Рассчитать"
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
    logging.info('We wait 30 seconds and click on the "Calculate" button')


# Проверяем новую дисанцию с известной нам
@then("Checking new total distance '{text}'")
def step(context, text):
    total_distance = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//span[@id="totalDistance"]'))
    )
    assert total_distance.text == text
    logging.info('Checking a new distance with a known to us')


# Проверяем новую цену с известной нам
@then("Checking new total price '{text}'")
def step(context, text):
    total_price = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "{}")]'.format(text)))
    )
    context.browser.implicitly_wait(10)
    assert re.search(text, total_price.text)
    logging.info('We check the new price with the known to us')
