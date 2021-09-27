#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time

#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Edge('C:/Users/PPSBn/msedgedriver.exe')

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("ttggno1@gmail.com")
password.clear()
password.send_keys("!=BDMP2r@$")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

#https://www.facebook.com/hashtag/bihu

#searching the hastag
# searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search Facebook']")))
searchbox.clear()
keyword = '#bihu'
searchbox.send_keys(keyword)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0,4000);")
posts = driver.find_elements(By.CSS_SELECTOR,"a[name='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']")
print(posts)
