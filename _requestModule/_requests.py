# Python kurulumuyla gelmeyen bir modül (request) pip install requests ile yükledik

# import json
                            # json modülünün konumuna baktık (deneme amaçlı)
# print(json.__file__)


import requests
import json

# result = requests.get("https://jsonplaceholder.typicode.com/todos")
# result = result.text # Adres üzerinden gelen json bilgi konsola yazıldı

# print(result) # Çıktı: <Response [200]> (Başarılı bir sonucun geldiğini söylüyor)
# print(type(result)) # str  print(result[0]["title"]) hata verir dolayısıyla

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

# print(result) # karmaşık gelir sonuçlar göz yorar

for i in result: # satır satır gelir
    if i["userId"] == 1:
        print(i["title"]) # sadece title'lar gelir

# print(result[0])
# print(result[0]["title"])
# print(type(result)) # list artık veri alabiliriz