from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


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

def printNycuNews(driver):
    driver.get("https://www.nycu.edu.tw/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element("link text","新聞").click()
    time.sleep(13)
    firstElementInNews = driver.find_element(By.CLASS_NAME, 'su-post')
    firstElementInNews.click()
    time.sleep(2)
    titleElementInNew = driver.find_element(By.CLASS_NAME, 'single-post-title.entry-title')
    print(titleElementInNew.text)
    bodyElementInNew = driver.find_element(By.CLASS_NAME, 'entry-content.clr')
    print(bodyElementInNew.text)

def searchInNewGoogleTab(driver, keyword):
    driver.switch_to.new_window("Tab2")
    driver.get("https://www.google.com/")
    time.sleep(1)
    driver.find_element(By.NAME,"q").send_keys(keyword)
    time.sleep(0.5)
    driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
    googleSearchSecond = driver.find_elements(By.CLASS_NAME, 'LC20lb.MBeuO.DKV0Md')[1]
    print(googleSearchSecond.text)

if __name__ == '__main__':
    driver = init_onGit()
    #driver = normal_init()
    
    printNycuNews(driver)
    time.sleep(2)
    searchInNewGoogleTab(driver, "311551169")
    driver.quit()