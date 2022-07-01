from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    num = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(str(calc(num)))
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(5)
    browser.quit()
