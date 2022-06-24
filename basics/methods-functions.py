# Methods

# python kütüphanesiyle beraber gelen yani önceden tanımlanmış şeyler. Örneğin string sınıfı, list sınıfının içinden gelen hazır metotlar

# from tkinter import Y


# list = [1, 2, 3]
# list.append(4) # append bir metottur ya da pop()

# Functions

# def sayHello(name = 'user'):
#     print('Hello ' + name)

# sayHello('Selim')
# sayHello() # Varsayılan olarak user gelir

# def sayHello(name = 'user'):
#     return 'Hello ' + name

# msg = sayHello()
# print(msg)

# def total(num1, num2):
#     return num1 + num2

# result = total(10, 20)
# print(result)

# def yasHesapla(dogumyili):
#     return 2022 - dogumyili

# ageSelim = yasHesapla(2002)
# ageTekin = yasHesapla(2003)

# print(ageSelim, ageTekin)

# def emeklilik(dogumYili, isim):
#     '''
#     DOCSTRING: Dogum yiliniza gore emekliliğinize kac yil kaldi
#     INPUT: Dogum yili
#     OUTPUT: Hesaplanan yil bilgisi
#     '''
#     yas = yasHesapla(1983)
#     emeklilik = 65 - yas

#     if emeklilik > 0:
#         print(f'Emekliliğe {emeklilik} yıl kaldı')
#     else:
#         print('Zaten emekli oldunuz')

# emeklilik(2002, 'Selim')
# print(help(emeklilik))

list = [1, 2, 3]

print(help(list.append))