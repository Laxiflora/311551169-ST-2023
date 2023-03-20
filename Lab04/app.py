from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
    WebDriverWait(driver, 60).until(lambda d:d.find_element(By.XPATH,'//a[@href="'+"https://www.nycu.edu.tw/news-network/"+'"]') ).click()

    WebDriverWait(driver, 60).until(lambda d:d.find_elements(By.XPATH, "//a[contains(@href, 'https://www.nycu.edu.tw/news/')]") )[1]
    firstElementInNews = driver.find_elements(By.XPATH, "//a[contains(@href, 'https://www.nycu.edu.tw/news/')]")[1]
    #print(f"element News title =  {firstElementInNews.text}")
    #print(f"element href = {firstElementInNews.get_attribute('href')}")
    firstElementInNews.click()
    #print(f"url should be 4537 :  {driver.current_url}")
    #driver.get("https://www.nycu.edu.tw/news/4537/")
    WebDriverWait(driver, 60).until(lambda d:d.find_element(By.CLASS_NAME, 'single-post-title.entry-title') )
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