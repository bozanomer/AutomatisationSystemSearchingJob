from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome("/Users/OBO/Desktop/chromedriver")
browser.get("https://www.linkedin.com/home")
browser.fullscreen_window()

time.sleep(3)

email=browser.find_element_by_xpath("//*[@id='session_key']")
password=browser.find_element_by_xpath("//*[@id='session_password']")

email.send_keys("bozan.omer@gmail.com")
password.send_keys("Orangeapple21213")

sigin=browser.find_element_by_xpath("//*[@id='main-content']/section[1]/div[2]/form/button")
sigin.click()

network=browser.find_element_by_xpath("//*[@id='ember22']") 
network.click()
time.sleep(5)

connections=browser.find_element_by_class_name("mn-community-summary__entity-info")
connections.click()

for i in range(1,4):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

connected_people=browser.find_elements_by_class_name("mn-connection-card__details")

connectedList=[]

for person in connected_people:
    connectedList.append(person.text)

with open ("connected.txt","w",encoding="UTF-8") as file:
    for person in connectedList:
        file.write(person + "\n")

time.sleep(5)

browser.quit()
