
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome("/Users/OBO/Desktop/chromedriver")
browser.get("https://www.linkedin.com/home")
browser.fullscreen_window()

time.sleep(3)

email=browser.find_element_by_xpath("//*[@id='session_key']")
password=browser.find_element_by_xpath("//*[@id='session_password']")

email.send_keys(input("Please enter your e-mail:") )
password.send_keys(input("Please enter your password:"))

time.sleep(3)

sigin=browser.find_element_by_xpath("//*[@id='main-content']/section[1]/div[2]/form/button")
sigin.click()



jobs=browser.find_element_by_xpath("//*[@id='ember24']/span")
jobs.click()

browser.implicitly_wait(20)
skills=browser.find_element_by_css_selector("#jobs-search-box-keyword-id-ember285")

time.sleep(3)
location=browser.find_element_by_css_selector("#jobs-search-box-location-id-ember285")

time.sleep(3)

skills.send_keys("Python")
time.sleep(3)
location.send_keys("Berlin")
time.sleep(3)
location.send_keys(Keys.RETURN)

browser.fullscreen_window()

time.sleep(4)
browser.quit()
