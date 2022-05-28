from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд
    location_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
    browser.find_element_by_id("book").click()
    #res
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    #sub
    browser.find_element_by_id('solve').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
