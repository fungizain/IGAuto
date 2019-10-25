import config
import time
from random import random
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def login(username, password):
    driver = config.DRIVER
    timeout = config.TIMEOUT
    try:
        driver.get(config.LOGIN_URL)
        driver.implicitly_wait(timeout)
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(username)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//form[@class='HmktE']/div[4]/button").click()
        
        WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="presentation"]')))
        time.sleep(1)
        driver.find_element_by_xpath('//div[@role="dialog"]/div/div[3]/button[2]').click()
        
    except TimeoutException:
        return False
    
#-----------func after login-----------
    
def explore():
    driver = config.DRIVER
    driver = config.TIMEOUT
    try:
        driver.get(config.HOST)
        driver.implicitly_wait(timeout)
        driver.find_element_by_xpath('//div[@class="XrOey"][1]/a').click()
        
    except TimeoutException:
        return False
    
def search(target):
    driver = config.DRIVER
    timeout = config.TIMEOUT
    
    try:
        WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
        ele = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        ele.send_keys(target)
        WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="drKGC"]')))
        
        ele.send_keys(Keys.ENTER)
        ele.send_keys(Keys.ENTER)
        
        WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element((By.XPATH, '//div[@class="nZSzR"]/h1'), target))
        
    except TimeoutException:
        return False

#-----------func after search-----------
    
def follow():
    driver = config.DRIVER
    timeout = config.TIMEOUT
    try:
        driver.implicitly_wait(timeout)
        ele = driver.find_element(By.XPATH, '//div[@class="nZSzR"]/div/span/span[1]/button')
        if ele.text == 'follow':
            ele.click()
        else: print("You already followed!")
    except NoSuchElementException:
        return False
    
def article(art_num):
    # post_num <= 24 otherwise need to scroll down a bit for more post link...
    driver = config.DRIVER
    timeout = config.TIMEOUT
    if not isinstance(art_num, int):
        art_num = int(art_num)
    row = art_num//3 if art_num%3 == 0 else art_num//3 + 1
    col = 3 if art_num%3 == 0 else art_num%3
    try:
        driver.find_element(By.XPATH, f'//article[@class="FyNDV"]/div[1]/div/div[{row}]/div[{col}]').click()
        WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, '//body[@style="overflow: hidden;"]')))
    except TimeoutException:
        pass

#-----------func after article-----------

def like_comment(like=False, comment=False, sentence='so cute!!', t=5):
    driver = config.DRIVER
    timeout = config.TIMEOUT
    if like:
        try:
            driver.find_element(By.XPATH, '//span[@aria-label="Like"]').click()
        except NoSuchElementException:
            return False
    if comment:
        try:
            driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]').click()
            WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, '//textarea[@data-focus-visible-added=""]')))
            driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]').send_keys(sentence)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        except TimeoutException:
            return False
    time.sleep(t*random())
    driver.find_element(By.XPATH, '//button[@class="ckWGn"]').click()

#-----------test-----------

if __name__ == '__main__':
    username = 'pm280090'
    password = 'priya1234'
    target = 'hangrydiary'
    login(username, password)
    search(target)
    follow()
    article(1)
    like_comment()
    
    