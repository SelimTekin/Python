import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')

list = soup.find_all("li",{"class":"column"}, limit=2)
count = 1

for li in list:
    
    if count == 2:
        name = li.div.a.h3.text.strip()
        link = li.div.a.get('href') # ürünün link bilgisi
        oldPrice = li.find("div", {"class":"priceContainer"}).find_all("span")[0].text.strip().strip('TL') # Çıktı: 7.999,00 
        newPrice =li.find("div", {"class":"priceContainer"}).find_all("span")[1].text.strip().strip('TL')
        # price = li.find("div", {"class":"priceContainer"}).find_all("span")[0].text
        print(f"name: {name}\nlink: {link}\nold price: {oldPrice}\nnew price: {newPrice}")
        break
    else:
        count += 1
    