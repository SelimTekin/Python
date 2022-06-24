# Gönderilern sınırsız sayıdaki parametreleri listeye ekleme

# def converter(*params): # *; snırsız sayıda paramtre
#     list = []
    
#     for param in params:
#         list.append(param)

#     return list

# result = converter(10, 20, 'Selim', True)
# print(result)

# ------------------------------------------------------------

# Gönderilen 2 sayı arasındaki asal sayıları bulma

# def asalBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2 + 1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if(sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input('sayı 1: '))
# sayi2 = int(input('sayı 2: '))
# asalBul(sayi1, sayi2)

# ------------------------------------------------------------

# Kendisine gönderilen bir sayının tam bölenlerini yazdırma

def tamBolenYazdir(sayi):
    tamBolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
    
    return tamBolenler

sayi = int(input('sayı: '))
result = tamBolenYazdir(sayi)
print(result)
