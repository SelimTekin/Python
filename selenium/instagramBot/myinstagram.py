from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'}) # İnstagramı ingilizce yaptık. Böylece hangi dil kullanılırsa kullanılsın İngilizce olacak yazılar.
        self.browser = webdriver.Chrome('../chromedriver.exe', chrome_options=self.browserProfile) # Oluşturduğumuz browser profile'ı driver ile ilişkilendirdik
        # self.browser = webdriver.Chrome("../chromedriver.exe")
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5) # 2 yapınca sayfa tam yüklenmiyor ve getFollowers() fonksiyonunda profil sayfasına gitmiyor

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)       # Sayfanın iyice yüklendiğinden emin olmak için 2 saniye bekliyoruz
        followersLink = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a')
        followersLink.click()
        time.sleep(2)

        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog] ul")
        followerCount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))
        print(f"first count: {followerCount}")


        # Çok fazla takipçi olduğunda scrollbar kaydırma işlemleri
        # action = webdriver.ActionChains(self.browser)

        # while True:
        # while followerCount < max: # istediğimiz sayıda takipçi
        #     dialog.click() # dialog ku2tusuna tıkladık ki scrollbar'ı aşağı indirebilelim
        #     action.key_down("\s").key_up("\s").perform() # SPACE tuşuna bastık
        #     time.sleep(2)

        #     newCount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))

        #     if followerCount != newCount:
        #         followerCount = newCount
        #         print(f"second count: {newCount}")
        #         time.sleep(1)
                
        #     else:
        #         break
            
        followers = dialog.find_elements(By.CSS_SELECTOR, "li")

        followerList = []
        # i = 0
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            followerList.append(link)
            # i += 1
            # if i >= max:
            #     break
        
        with open("followers.txt", "w", encoding="utf-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUser(self, username):
        self.browser.get("https://instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unfollowUser(self, username):
        self.browser.get("https://instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
        if followButton.text != "Follow":
            followButton.click()
            time.sleep(2)
            # bu satırın sonunda click() metodu var gözden kaçmasın :)
            self.browser.find_element(By.XPATH, "//button[text()='Unfollow']").click()
        else:
            print("Zaten takip etmiyorsunuz")

instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollowers()
# instagram.followUser("kod_evreni")
# instagram.unfollowUser("kod_evreni")

# Birden fazla takip için
# lis = ["kod_evreni",""]     

# for user in list:
#     instagram.followUser(user)
#     time.sleep(3)