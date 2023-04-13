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


    select = Select(driver.find_element_by_id("language_select"))

# select by visible text
#select.select_by_visible_text("Traditional Chinese")

# select by value 
    select.select_by_value('zh-tw')



if __name__ == '__main__':
    #driver = init_onGit()
    driver = normal_init()
    
    Q2_1(driver)
    time.sleep(2)
    driver.quit()