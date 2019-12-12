from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def check(url, email, password):
    driver = webdriver.Chrome('./chromedriver')
    homePage = driver.get(url)
    assert "signin" or "login" in driver.title
    log_page = driver.title
    wait = WebDriverWait(driver, 5)
    wait.until(ec.frame_to_be_available_and_switch_to_it)
    emailBar = driver.find_element_by_css_selector('input[type="email"]')
    passwordBar = driver.find_element_by_css_selector('input[type="password"]')

    #captcha = driver.find_element_by_css_selector('span[role="checkbox"]')
    logForm = driver.find_elements_by_tag_name('form')
    checkboxes = driver.find_elements_by_css_selector('[type="checkbox"]')

    for checkbox in checkboxes:
        checkbox.click()

    #captcha.click()

    emailBar.clear()
    passwordBar.clear()
    emailBar.send_keys(email)
    passwordBar.send_keys(password)
    logForm[0].submit()
    assert "page not found" not in driver.page_source
    if driver.title == log_page:
        global status
        status='Bad'
    else:
        status="Good"
    print(driver.page_source)
    driver.close()
    return status



