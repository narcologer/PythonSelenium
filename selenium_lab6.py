from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time

def clicknwrite(driver):
    song_title = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[1]/span[1]').text
    artist = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/a').text
    button = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/button[3]').click()
    print(song_title+' '+artist)
    time.sleep(2)
    

driver = webdriver.Firefox()
driver.get("https://vk.com/")

email = driver.find_element_by_xpath("//*[@id=\"index_email\"]")
password = driver.find_element_by_xpath("//*[@id=\"index_pass\"]")

loginButton = driver.find_element_by_xpath("//*[@id=\"index_login_button\"]")

resource = open("./loginpass.txt").readlines()

email.send_keys(resource[0])
password.send_keys(resource[1])
loginButton.click()

element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[1]/div/nav/ol/li[7]/a/span/span[3]"))
    )

element.click()

element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/button[3]'))
    )

button = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/button[1]').click()

time.sleep(2)
for i in range(10):
    clicknwrite(driver);
button = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/button[3]').click()
driver.quit();
