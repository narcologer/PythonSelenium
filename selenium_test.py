from selenium import webdriver

driver = webdriver.Firefox();
driver.get('https://www.smwcentral.net/');

print (driver.title);
print (driver.current_url);

driver.quit();
