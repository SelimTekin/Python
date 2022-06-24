
# Bu kodlar web scraping örneğidir

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content # html sayfa kaynağı geldi (yani sayfanın tüm html etiketleri)

soup = BeautifulSoup(html, 'html.parser')

list = soup.find("tbody", {"class":"lister-list"}).find_all('tr', limit=50) # class'ı lister-list olan tbody etiketinin içinden 50 adet tr etiketini alır
count = 1
for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text # Çıktı: The Shawshank Redemption
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()") # strip ile parantezleri sildik # Çıktı: The Shawshank Redemption 1994
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text

    print(f"{count} - film: {title.ljust(50,'*')} yıl: {year} değerlendirme: {rating}") # ljust ile 50 karakterde sola yasladık
    count += 1