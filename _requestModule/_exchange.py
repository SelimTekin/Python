import requests
import json

# API_KEY kısmına siteye kaydolup api key alıp yazmanız lazım
# api_url = "https://api.exchangeratesapi.io/v1/latest?access_key=soJKYZq4ern4UofbC2VKpqVRfCbED4Ac&base=" # eşittirden sonraki kısım boş olsun ki istediğimizi girebilelim(normalde USD yazıyordu (dolar))


bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

api_url = f"https://api.apilayer.com/exchangerates_data/convert?to={alinan_doviz}&from={bozulan_doviz}&amount={miktar}"

payload = {}
headers= {
  "apikey": "soJKYZq4ern4UofbC2VKpqVRfCbED4Ac"
}


response = requests.request("GET", api_url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
result = json.loads(result)

print(result["result"])
# print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz], alinan_doviz))
# print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz,miktar * result["rates"][alinan_doviz], alinan_doviz))


# url = "https://api.apilayer.com/exchangerates_data/convert?to=TRY&from=USD&amount=amount"

# payload = {}
# headers= {
#   "apikey": "soJKYZq4ern4UofbC2VKpqVRfCbED4Ac"
# }

# response = requests.request("GET", url, headers=headers, data = payload)

# status_code = response.status_code
# result = response.text