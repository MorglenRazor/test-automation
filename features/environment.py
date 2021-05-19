import logging
import platform
import configparser

from selenium.webdriver.chrome import webdriver
from selenium import webdriver


def check_system(context,config):
    if platform.system() == 'Linux':
        print("OS LINUX")
        linix_path = config['PATH']
        executable_path = linix_path['LinuxPathChromeDriver']
        opts = webdriver.ChromeOptions()
        context.browser = webdriver.Chrome(executable_path=executable_path, options=opts)  # options=opts
        str1 = context.browser.capabilities['browserVersion']
        str2 = context.browser.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        if str1[0:2] != str2[0:2]:
            print("Верия chromedriver не соответствует браузеру")
            print("Верия chromedriver {}".format(str1[0:2]))
            print("Верися Браузера {}".format(str2[0:2]))
            print("Скачайте соответствующую версияю и положите в папку res")
    else:
        print("OS Windows")
        linix_path = config['PATH']
        executable_path = linix_path['WindowsPathChromeDriver']
        opts = webdriver.ChromeOptions()
        context.browser = webdriver.Chrome(executable_path=executable_path, options=opts)  # options=opts
        str1 = context.browser.capabilities['browserVersion']
        str2 = context.browser.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        if str1[0:2] != str2[0:2]:
            print("Верия chromedriver не соответствует браузеру")
            print("Верия chromedriver {}".format(str1[0:2]))
            print("Верися Браузера {}".format(str2[0:2]))
            print("Скачайте соответствующую версияю и положите в папку res")
    return context.browser


def before_scenario(context, scenario):

    config = configparser.ConfigParser()
    config.read('res/config.ini')
    config.sections()
    context.browser = check_system(context, config)


def after_scenario(context, scenario):
    context.browser.quit()
