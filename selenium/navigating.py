from selenium import webdriver
import time
from selenium.webdriver.common.by import By     # find_element(By.NAME) -> Buradaki By'ı kullanabilmek için import ettik
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME, 'q')     # path ile de yapılabilir (alt satırda)
# searchInput = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

# result = driver.page_source       # Alternatif yol
# print(result)

result = driver.find_elements(By.CSS_SELECTOR,".repo-list-item a")

for element in result:
    print(element.text)
driver.close()