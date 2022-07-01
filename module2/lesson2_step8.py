from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson2_step8.txt')  # добавляем к этому пути имя файла

    browser.find_element(By.NAME, "firstname").send_keys("qqbb")
    browser.find_element(By.NAME, "lastname").send_keys("359")
    browser.find_element(By.NAME, "email").send_keys("qqbb359@mail.ru")

    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(5)
    browser.quit()
