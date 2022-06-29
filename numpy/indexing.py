import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[5] # 5. indeksteki eleman gelir
result = numbers[-1] # en sondaki eleman gelir
result = numbers[0:3] # 0'dan 3'e kadar olan sayılar gelir
result = numbers[:3] # aynı
result = numbers[3:] # 3'ten sona
result = numbers[::] # hepsi
result = numbers[::-1] # tersten hepsi
result = numbers[::-2] # tersten hepsi (2'şer 2'şer yani birini alır birini almaz)

numbers = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])    # Üçü de birer satır oluyor
result = numbers[0] # Çıktı: [ 0  5 10] (aslında 0. satırı temsil ediyor)
result = numbers[2]
result = numbers[0, 2] # 10 (aslında 0 -> satır, 2 -> sütun oluyor)
result = numbers[2, 1] # 75
result = numbers[:,2] # Çıktı: [10 25 85] (bütün satırların 2. indeksindeki sayıları alır. Gelen değerler yeni bir dizi içerisinde gelir)
result = numbers[:,0] # Çıktı: [ 0 15 50] (bütün satırların 0. indeksindeki sayıları alır. Gelen değerler yeni bir dizi içerisinde gelir)
result = numbers[:,0:2] # Çıktı: [[ 0  5]
                                # [15 20]
                                # [50 75]]      # 0-2 arası elemanları alır

result = numbers[-1,:] # Çıktı: [50 75 85] (son satırdaki tüm sütunları alır)
result = numbers[:2,:2] # Çıktı: [[ 0  5]
                                # [15 20]] (0-2 arası satırlardaki 0-2 arası sütunları alır)

# print(result)

arr1 = np.arange(0,10)
arr2 = arr1     # referans kopyalaması yaptık
arr2 = arr1.copy() # aynı referansa sahip değil. Dolayısıyla arr2 yapılna değişiklik arr1'i etkilemeyecek
# print(arr1)
# print(arr2) # aynı

arr2[0] = 20

print(arr1)
print(arr2) # yine aynı referansları aynı çünkü (0. indeks 20 oldu)