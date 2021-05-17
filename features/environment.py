from selenium.webdriver.chrome import webdriver
from selenium import webdriver


def before_scenario(context, scenario):
    capabilities = {
        "browserName": "chrome",
        "version": "90.0",
        "platform": "LINUX"
    }

    context.browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )


def after_scenario(context, scenario):
    context.browser.quit()
