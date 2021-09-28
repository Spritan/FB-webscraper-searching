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

# posts_detected = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.__class__,'j83agx80 cbu4d94t obtkqiv7 sv5sfqaa')))
time.sleep(5)

posts = driver.find_element_by_xpath("//*/span/a/strong/span")
print(posts.text)

# try:
#     posts = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME,"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 embtmqzv fe6kdd0r mau55g9w c8b282yb hrzyx87i m6dqt4wy h7mekvxk hnhda86s oo9gr5id hzawbc8m"))
#     )
#     posts = driver.find_element_by_xpath("//*/span/a/strong/span")
#     print(posts.text)
# except:
# driver.execute_script("window.scrollTo(0,4000);")
#     posts = driver.find_element_by_xpath("//*/span/a/strong/span")
#     print(posts.text)
# driver.quit()
