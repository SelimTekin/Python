# ---------------------- Dosya adını module adıyla aynı yapma hata alabilirsin (o yüzden _random yaptık) ----------------------

import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100 + 10 # 10.0 - 100.0 (başlangıç 10 olur bu şekilde)
result = int(random.uniform(10,100)) # aralık belirtiyoruz
result = random.randint(1,100) # her iki sınır da dahil (anladığım kadarıyla)

greeting = 'hello there'
names = ['ali', 'yağmur', 'deniz', 'cenk', 'ahmet', 'efe']
result = names[random.randint(0, len(names) - 1)]

result = random.choice(names) # kendi random eleman seçiyor
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste) # elemanları karıştırılmış liste
result = liste

liste = range(100) # Çıktı: range(0, 100)
result = random.sample(liste, 3) # listeden rastgele 3 eleman alıyor
result = random.sample(names, 2) # names listesinden rastgele 2 isim seçti

print(result)