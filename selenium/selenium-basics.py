from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2) # 2 saniye bekledi
driver.maximize_window() # tarayıcı tam ekran oldu
driver.save_screenshot("github.com-homepage.png") # github anasayfa screenshot aldı

url = "http://github.com/SelimTekin"
driver.get(url)

print(driver.title) # sayfanın title'ını yazdı

if "SelimTekin" in driver.title:
    driver.save_screenshot("github-SelimTekin.png")

time.sleep(2)
driver.back() # Önceki sayfaya gider
# driver.forward() # Sonraki sayfaya gider
time.sleep(2)

driver.close() # tarayıcı kapandı