from datetime import date, datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import schedule
import threading
import random

def test(bien1, bien2):
    ignored_exceptions=(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException,)
    while datetime.now().minute in range(45) or datetime.now().minute in range(57,60):
        try:
            element = WebDriverWait(bien1, 2500, ignored_exceptions=ignored_exceptions).until(
                                    EC.presence_of_element_located((By.CLASS_NAME, bien2)))
        except TimeoutException:
            return
        return element

def bamLiXi(tk):
    if datetime.now().hour in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return
    ran = random.randint(2, 5)
    driver = webdriver.Chrome('chromedriver.exe')
    time.sleep(ran)
    driver.get('https://loto567.com/')
    time.sleep(ran)
    login = driver.find_element_by_xpath("//button[@class='el-button login el-button--default']")
    login.click()
    time.sleep(ran)
    taikhoan = driver.find_element_by_xpath("//input[@class='el-input__inner']")
    taikhoan.send_keys(tk[0])
    time.sleep(ran)
    matkhau = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/form/div[2]/div/div/input")
    matkhau.send_keys(tk[1])
    time.sleep(ran)
    login2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/span/button")
    login2.click()
    
    # while 1:
    time.sleep(ran)
    driver.refresh()
    time.sleep(ran)
    driver.find_element_by_class_name("chatRoomButton").click()
    # lixi = driver.find_element_by_class_name("redBagWrap")
    # lixi = test(driver, "redBagWrap")
    mo = driver.find_element_by_class_name("openBtn")
    while datetime.now().minute in range(45) or datetime.now().minute in range(57,60):
        try:
            driver.find_element_by_class_name("redBagWrap").click()
            for i in range(5):
                try:
                    mo.click()
                except:
                    continue
            break
        except:
            continue
    time.sleep(30)
    # mo = test(driver, "getRedPackImgCon")
    print('thanhcong '+tk[0])
    print(datetime.now())
    return
        # while datetime.now().minute != 57:
        #     continue

def run_threaded(tk):
    for i in tk:
        job_thread = threading.Thread(target=bamLiXi, args=(i,))
        job_thread.start()
        time.sleep(30)

if __name__ == '__main__':
    taikhoan = [['buibappp', 'Kiemtie99n'], ['buibapppp', 'Kiemtie99n']]
    schedule.every().hour.at('57:00').do(run_threaded, [['thamm08', 'Kiemtie99n']])
    while True:
        schedule.run_pending()
        time.sleep(1)