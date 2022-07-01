from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    answer = calc(num)
    browser.find_element(By.ID, "answer").send_keys(answer)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    time.sleep(5)
    browser.quit()
