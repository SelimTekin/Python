# x = 1

# while x <= 100:
#     if (x % 2 == 1):
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += 1
# print(x) # Çıktı: 101

# name = '' # False
# if name == True:
#     print('True')
# else:
#     print('False')
    
# while not name.strip(): # name False olduğu için döngüye girdi çünkü koşul False olması
#     name = input('isminizi giriniz: ') # name True oldu ve döngü kırıldı

# print(f'Merhaba {name}')

# numbers = []

# i = 0

# while i<5:
#     sayi = int(input('sayı: '))
#     numbers.append(sayi)
#     i += 1

# numbers.sort() # Rastgele girilen sayıları sıraladık
# print(numbers)

urunler = []

adet = int(input('kaç adet ürün eklemek istiyorsunuz: '))
i = 0

while i<adet:
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name':name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')