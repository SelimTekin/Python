from hashlib import new
from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# twitterUserInfo modülünde kullanıcı adı ve şifre giriniz !

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"}) # Tarayıcıyı kabul ettiğimiz dil ingilizce olsun(US ingilzicesi)
        self.browser = webdriver.Chrome("../chromedriver.exe", chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        # username girilip tıklanmadan şifre inputu görünmüyor
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)

        passwordInput = self.browser.find_element(By.NAME, "password")        
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(2)

    def search(self, hashtag):
        searchInput = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        
        results = []

        list = self.browser.find_elements(By.XPATH, "//article[@data-testid='tweet']/div/div/div/div[2]/div[2]/div[2]/div/div") # attribute'a göre bu kullanılır
        time.sleep(2)
        print("count: " + str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0
        # scrollbar yüksekliği
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight") # Javascript kodlarını çalştırmak için.
        while True:
            if loopCounter > 3: # python popüler bi kleime olduğu için scroll'u sınırlandırdık
                break
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1

            list = self.browser.find_elements(By.XPATH, "//article[@data-testid='tweet']/div/div/div/div[2]/div[2]/div[2]/div/div") # attribute'a göre bu kullanılır
            time.sleep(2)
            print("count: " + str(len(list)))

            for i in list:
                results.append(i.text)
            
            count = 1
            with open("tweets.txt", "w", encoding="utf-8") as file:
                for item in results:
                    file.write(f"{count} - {item}\n")
                    count += 1
        # count = 1
        # for item in results:
        #     print(f"{count} - {item}")
        #     count += 1
        #     print("****")


twitter = Twitter(username, password)

# login

twitter.signIn()
twitter.search("python")
