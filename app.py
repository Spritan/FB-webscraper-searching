#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

tag = input("Enter the hashtag = #",)
n_scrolls = int(input("Enter the number how much the page to be scrolls down : "))

#code by stack overflow, not me

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# System.setProperty("webdriver.chrome.driver", "C:/Users/ritav/Downloads/Driver_Notes/msedgedriver.exe");
# ChromeOptions chromeOptions = new ChromeOptions();
# chromeOptions.setBinary("C:\\Program Files (x86)\\Microsoft\\Edge Dev\\Application\\msedge.exe");
# chromeOptions.setExperimentalOption("useAutomationExtension", false);
# chromeOptions.setExperimentalOption("excludeSwitches", Collections.singletonList("enable-automation"));
# ChromeDriver driver = new ChromeDriver(chromeOptions);
# driver.get("http://www.google.com");
# driver.close();

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/ritav/Downloads/chromedriver.exe', options = chrome_options)

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


posts = driver.find_element_by_XPath("//*[@id='jsc_c_93']/div/div/span/div[1]/div/text()")
print(posts)


#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "search[class='o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'']")))
#posts = driver.find_element_by_xpath("")
#print(posts)


#class="o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"
#class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"
