from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


def normal_init():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
    return driver

def init_onGit():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)
    return driver

def Q2_1(driver):
    driver.get("https://docs.python.org/3/tutorial/index.html")
    #driver.find_element(By.CLASS_NAME, "language_switcher_placeholder").click()
    #select = Select(driver.find_element(By.CLASS_NAME, "language_switcher_placeholder"))

    #for op in select.options:
        #print(op.text)

# select by visible text
    #select.select_by_visible_text("Traditional Chinese")


def Q2_2(driver):
    driver.get("https://docs.python.org/3/tutorial/index.html")
    time.sleep(0.5)
    driver.find_elements(By.NAME,"q")[1].send_keys("class")
    time.sleep(0.5)
    driver.find_elements(By.NAME,"q")[1].send_keys(Keys.ENTER)
    #time.sleep(60)
    #driver.find_elements(By.CLASS_NAME, "search-summary").text
    #WebDriverWait(driver, 60).until(lambda d:d.find_elements(By.CLASS_NAME, "search-summary")[0].text != "&nbsp" )[1]


if __name__ == '__main__':
    driver = init_onGit()
    #driver = normal_init()
    
    Q2_1(driver)
    Q2_2(driver)
    time.sleep(2)
    driver.quit()