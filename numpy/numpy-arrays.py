from xml.dom import NAMESPACE_ERR
import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1, 10) # Çıktı: [1 2 3 4 5 6 7 8 9]
# result = np.arange(10, 100, 3) # 10'dan 100'e kadar üçer üçer artan dizi
# result = np.zeros(10) # Çıktı: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] (float değerler olduğu için yanlarında nokta var)
# result = np.ones(10) # Çıktı: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] (float değerler olduğu için yanlarında nokta var)
# result = np.linspace(0, 100, 5) # Çıktı: [  0.  25.  50.  75. 100.] (5 eşit parçaya böler)(lin -> linear)
# result = np.linspace(0, 5, 5) # Çıktı: [0.   1.25 2.5  3.75 5.  ] (5 eşit parçaya böler)
# result = np.random.randint(0, 10) # 0 ile 10 arasında random sayı üretir (random dosaysındaki randint metodu)
# result = np.random.randint(20) # 0 ile 20 arasında
# result = np.random.randint(1, 10, 3) # 0 ile 10 arasında 3 adet sayı üretir dizi olarak
# result = np.random.rand(5) # Çıktı: [0.40964218 0.33666311 0.47270562 0.31688723 0.0258098 ] (0 ile 1 arasında 5 adet sayı üretir)
# result = np.random.randn(5) # Çıktı: [ 0.41364223 -1.25546451 -1.53903839  0.8766609  -1.07805862] (eksi değerler dahil 0 ile 1 arasında 5 adet sayı üretir)
# np_array = np.arange(50) # 0'dan 50'ye kadar olan sayıları dizide oluşturur
# np_multi = np_array.reshape(5, 10) # 5 satır 10 sütun
# print(np_multi.sum(axis=1)) # Çıktı: [ 45 145 245 345 445] (satırların toplamı gelir)
# print(np_multi.sum(axis=0)) # Çıktı: [100 105 110 115 120 125 130 135 140 145] (sütunların toplamı gelir)

rnd_numbers = np.random.randint(1, 100, 10) # 1-100 arası 10 adet sayı
print(rnd_numbers)
result = rnd_numbers.max() # maksimum sayı gelir
result = rnd_numbers.min() # minimum sayı gelir
result = rnd_numbers.mean() # dizinin ortalaması gelir
result = rnd_numbers.argmax() # en büyük sayının indeksi gelir
result = rnd_numbers.argmin() # en küçük sayının indeksi gelir

print(result)