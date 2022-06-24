# def changeName(n): # n ile name farklı adresler tutar. n adres kopyalamsı yapar
#     n = 'ada'

# name = 'Selim'
# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']
# n = sehirler[:] # slicing. sehirler dizisindeki bütün elemanları n değişkenine attık. adres kopyalaması değil de value type larda olduğu gibi kopyalama işlemi yapmış oluyoruz

# change(sehirler[:])
# print(sehirler) # dizi bozulmamış olur Çıktı: ['ankara','izmir']

# change(sehirler) # sehirler dizisinin adresini alır
# print(sehirler) # Çıktı: ['istanbul','izmir']
# print(n) # Çıktı: ['ankara','izmir']


# def add(*params): # *params, içine kaç tane parametre gönderilirse ona göre işlem yapar.(tuple listesi) Tek tek parametre belirlemek yerine kullanılır çok parametreli olduğu zaman
#     print(type(params)) # Çıktı: <class 'tuple'> yani tuple tipinde
#     print(params[0])
#     return sum(params) # sum(), gömülü fonksiyondur. adı üstünde toplama yapar.

# print(add(10,20,30))

# def displayUser(**args): # ** (çift yıldız); dictionary olduğunu belirtir. Farklı parametre türleri olduğunda key,value kullanabilmek için.
#     print(type(args)) # Çıktı: <class 'dict'> yani dictionary tipinde
#     for key,value in args.items():
#         print('{} is {}'.format(key,value))

# displayUser(name = 'Selim', age = 19, city = 'İstanbul')
# displayUser(name = 'Tekin', age = 20, city = 'Sinop')
# displayUser(name = 'Yavuz', age = 21, city = 'Kırklareli')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, key1 = 'value1', key2 = 'value2')