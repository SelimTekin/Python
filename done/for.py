numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num) # Çıktı: 1 2 3 4 5
    print('Hello') # 5 defa Hello yazar

names = ['Selim', 'Tekin']

for name in names:
    print(f'My name is {name}')

name = 'Selim Tekin' # String, bir dizi olduğu için harfleri tek tek alt alta yazdırır

for n in name:
    print(n)

tuple = [(1,2), (1,3), (3,5), (5,7)]

for a,b in tuple:
    #print(t) # Çıktı: (1,2) (1,3) (3,5) (5,7) alt alta
    print(a,b) # Çıktı: 1 2 / 1 3 / 3 5 / 5 7 (alt alta)
    #print(a) # Çıktı: 1 1 3 5 (alt alta)


d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d.items():
    print(item) # Çıktı: k1 k2 k3 ( sadece d yazdığında ) alt alta
    print(item) # Çıktı: ('k1': 1) / ('k2': 2) / ('k3': 3)

urunler = [
    {'name':'samsung S6', 'price':'3000'},
    {'name':'samsung S7', 'price':'4000'},
    {'name':'samsung S8', 'price':'5000'},
    {'name':'samsung S9', 'price':'6000'},
    {'name':'samsung S10', 'price':'7000'},
]

toplam = 0
for urun in urunler:
    print(urun['price']) # Fiyatlar yazar
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)

for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])