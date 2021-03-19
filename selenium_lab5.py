from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import random
import threading
import time

def test1():
    element = driver.find_element_by_id("num")
    element.send_keys(10)
    element = driver.find_element_by_id("st")
    element.send_keys(7)
    element = driver.find_element_by_id("en")
    element.send_keys(666)
    butt = driver.find_element_by_id("go")
    butt.click()

def test2():
    element = driver.find_element_by_id("num")
    element.clear()
    element.send_keys(10)
    element = driver.find_element_by_id("st")
    element.clear()
    element.send_keys(7)
    element = driver.find_element_by_id("en")
    element.clear()
    element.send_keys(666)
    element = driver.find_element_by_id("rpt")
    element.send_keys('Unique Values')
    butt = driver.find_element_by_id("go")
    butt.click()
    

driver = webdriver.Firefox()
driver.get("https://psychicscience.org/random")
test1();
time.sleep(3)
test2();
time.sleep(3)
driver.quit();


