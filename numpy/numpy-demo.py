import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
result = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
result = np.arange(5, 15) # [ 5  6  7  8  9 10 11 12 13 14]

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
result = np.arange(50, 100, 5) # [50 55 60 65 70 75 80 85 90 95]

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result = np.zeros(10) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
result = np.ones(10) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
result = np.linspace(0, 100, 5) # [  0.  25.  50.  75. 100.]

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
result = np.random.randint(10, 30, 5) # [27 29 27 17 22] (random dosaysındaki randint metodu)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
result = np.random.randn(10) # [ 0.40302183  0.58901358 -1.05122806  0.13846591 -0.30725758 -0.70602306 -0.29532157  0.95231187  0.94735459 -0.72942928] (n ile 0-1 arası eksiler de dahil)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
# result = np.random.randint(10, 50, 15).reshape(3, 5) # (50 dahil değil)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?
matris = np.random.randint(10, 50, 15).reshape(3, 5)
print(matris)
# rowTotal = matris.sum(axis = 1) # [128 201 120] (satırlardaki elemanlar toplamı)
# colTotal = matris.sum(axis = 0) # [ 78 130  79 100  62] (sütunlardaki elemanlar toplamı)
# print(matris)
# print(rowTotal)
# print(colTotal)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
result = matris.max()
result = matris.min()
result = matris.mean()

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?
result = matris.argmax()
result = matris.argmin()

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
arr = np.arange(10, 20)
print(arr)

result = arr[0:3]
result = arr[:3] # aynı

# 14- Üretilen dizinin elemanlarını tersten yazdırın.
result = arr[::-1]

# 15- Üretilen matrisin ilk satırını seçiniz.
result = matris[0]

# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?
result = matris [1, 2]

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
result = matris[:,0]

# 18- Üretilen matrisin her bir elemanının karesini alınız.
result = matris ** 2

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? 
#     Aralığı (-50,+50) arasında yapınız.

matris = np.random.randint(-50, 50, 15).reshape(3, 5)

ciftler = matris[matris % 2 == 0] # True olanlar çiftler olacak ve o değerler yazılacak
result = ciftler[ciftler > 0]

print(result)