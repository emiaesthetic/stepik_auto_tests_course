from selenium.webdriver.common.by import By

def test_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    cart = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(cart) > 0, "Нет кнопки добавить в корзину"
