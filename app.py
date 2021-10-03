#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

tag = input("Enter the hashtag = #",)
n_scrolls = int(input("Enter the number how much the page to be scrolls down : "))

#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("xabcd989@gmail.com")
password.clear()
password.send_keys("Abcdxyz989@")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

#To search hashtag
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search Facebook']")))
search.clear()
search.send_keys(tag)

#To open the hashtag page
for i in [tag]:
    driver.get('https://www.facebook.com/hashtag/' + tag + '/')
    time.sleep(5)

#for i in [tag]:
#    driver.get('https://www.facebook.com/hashtag/%23kidsfestival%20%23online%20%23digitalfestival%20%23talentedpeople/')
#    time.sleep(5)

#https://www.facebook.com/hashtag/%23kidsfestival%20%23online%20%23digitalfestival%20%23talentedpeople/
#kidsfestival2021 #online #digitalfestival #talentedpeople

#How much scrolls you need
    for j in range(0, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)


posts = driver.find_element_by_css_selector("span > a > strong > span")
print(posts.text)


#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "search[class='o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'']")))
#posts = driver.find_element_by_xpath("")
#print(posts)


#class="o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"
#class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"
