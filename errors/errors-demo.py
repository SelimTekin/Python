# liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputu sayı olduğundan emin olun aksi halde hata mesajı yazın

# while True:
#     sayi = input("sayı: ")
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print("girdiğiniz sayı: ", result)
#         break
#     except ValueError:
#         print("geçersiz sayı")
#         continue

# 3: Girilen parola içinde türkçe hatası veriniz

# def check_password(psw):
#     turkce_karakterler = 'şçğüöıİ'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError("Parola Türkçe karakter içeremez")
#         else:
#             pass
#     print("geçerli parola")

# parola = input("parola: ")

# try:
#     check_password(parola)
# except TypeError as err:
#     print(err)

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin

def faktoriyel(x):
    try:
        x = int(x)
    except:
        raise ValueError("Rakam olmalı")

    if x < 0:
        raise ValueError("Negatif değer")
    
    result = 1

    for i in range(1, x+1):
        result *= i
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)