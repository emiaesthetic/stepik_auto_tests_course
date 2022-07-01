from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(result)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()