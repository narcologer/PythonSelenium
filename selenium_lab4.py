from selenium import webdriver
from selenium.common.exceptions import *
cutie = "https://i.pinimg.com/originals/03/6b/c1/036bc18082a8322c39afc861e59c188e.jpg";


driver = webdriver.Firefox();

l = []
f = open('D:\sitelist.txt', 'r')
l = f.read().split('*')
f.close()
f = open('D:\sitelistout.txt', 'w')
for s in l:
    driver.get(s);
    elements = driver.find_elements_by_tag_name('img')
    for i in elements:
        img_src = i.get_attribute('src')
        if (img_src == cutie):
            f.write(driver.current_url);      
f.close();
driver.quit();
