# -------------- Sayı Tahmin Oyunu --------------

# import random # https://medium.com/python/python-random-mod%C3%BCl%C3%BC-a0de3ec02ff sitesinde random modülü fonksiyonları anlatılıyor

# # sayi = random.random() # 0.0 ile 1.0 arasında rastgele sayı üretir
# sayi = random.randint(1, 10) # 1 ile 100 arasında rastgele sayı üretir
# can = int(input('Kaç hak kullanmak istersiniz: '))
# hak = can
# sayac = 0
# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('tahmin: '))

#     if tahmin == sayi:
#         print(f'Tebrikler {sayac}. defada doğru bildiniz. Puanınız {100 - (100/can) * (sayac - 1)}')
#         break
#     elif tahmin < sayi:
#         print('yukarı')
#     else:
#         print('aşağı')

#     if hak == 0:
#         print(f'Hakkınız bitti sayı: {sayi}')

# -------------- Asal sayı kontrolü --------------

sayi = int(input('sayı giriniz: '))
asalMi = True

if sayi == 1:
    asalMi = False

for i in range(2, sayi):
    if sayi % i == 0:
        asalMi =False
        break

if asalMi:
    print('Sayı asaldır')
else:
    print('Sayı asal değildir')
