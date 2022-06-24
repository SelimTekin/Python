html_doc = """"

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Eğitim Sayfası</title>
</head>
<body>
    <h1 id="header">Python Eğitimi</h1>

    <div class="grup1">
        <h2>Programlama</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>Modüller</h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>Django</h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="Fred_Cakmaktas.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') # pars etme(html dokümanı olarak editleme)

result = soup.prettify() # düzensiz olan html dokümanını düzenli hale getirir(mesela meta ve ul etiketleri içeri kaymış dikkatli bakarsan)
result = soup.title # sayfanın title etiketi gelir # Çıktı: <title>Python Eğitim Sayfası</title>
result = soup.head
result = soup.body

result = soup.title.name # Etiket ismi gelir # Çıktı: title
result = soup.title.string # İçerisindeki ifadeyi getirir # Çıktı: Python Eğitim Sayfası

result = soup.h1 # Çıktı: <h1 id="header">Python Eğitimi</h1>
result = soup.h2 # Sayfada 2 tane var ve ilk h2 etiketi gelir # Çıktı: <h2>Programlama</h2>
result = soup.h2.name # Çıktı: h2
result = soup.h2.string # Çıktı: Programlama
result = soup.h1.string # Çıktı: Python Eğitimi

result = soup.find_all('h2') # liste halinde tüm h2 etiketleri gelir # Çıktı: [<h2>Programlama</h2>, <h2>Modüller</h2>]
result = soup.find_all('h2')[0] # İlk h2 etiketi # Çıktı: <h2>Programlama</h2>
result = soup.find_all('h2') # İkinci h2 etiketi # Çıktı: <h2>Modüller</h2>

result = soup.div # ilk div etiketi
result = soup.find_all('div')[1] # İkinci div etiketi
result = soup.find_all('div')[1].ul.find_all('li') # İkinci div etiketinin içindeki ul etiketinin içindeki :) tüm li etiketleri # Çıktı: [<li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]

result = soup.div.findChildren() # div etiketi altındaki tüm alt elemanlar gelir

result = soup.div.findNextSibling().findNextSibling().findPreviousSibling() # Next bir sonraki, previous bir önceki konuma gider. Dolayısıyla bu 2. div oluyor

result = soup.find_all('a')
for link in result:
    print(link.get('href')) # a etiketleri içindeki linkleri tek tek aldık # Çıktı: http://example1.com/elsie (3 adet çıkar)

print(result)