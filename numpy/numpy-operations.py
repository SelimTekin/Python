import numpy as np

numbers1 = np.random.randint(10, 100, 6) # 10-100 arası 6 adet sayı
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2    # aynı indeksteki elemanları toplar ve bir diziye atar
result = numbers1 - numbers2    # aynı indeksteki elemanları çıkarır ve bir diziye atar
result = numbers1 * numbers2    # aynı indeksteki elemanları çarpar ve bir diziye atar
result = numbers1 / numbers2    # aynı indeksteki elemanları böler ve bir diziye atar
result = numbers1 + 10    # her indeksteki elemanlara 10 ekler ve bir diziye atar
result = numbers1 - 10    # her indeksteki elemanlardan 10 çıkarır ve bir diziye atar
result = numbers1 * 10    # her indeksteki elemanlardan 10 ile çarpar ve bir diziye atar
result = numbers1 / 10    # her indeksteki elemanlardan 10'a böler ve bir diziye atar

result = np.sin(numbers1) # her elemanın sinüsünü alır
result = np.cos(numbers1) # her elemanın kosinüsünü alır
result = np.sqrt(numbers1) # her elemanın karekökünü alır
result = np.log(numbers1) # her elemanın logaritmasını alır

mnumbers1 = numbers1.reshape(2, 3)
mnumbers2 = numbers2.reshape(2, 3)

# print(mnumbers1)
# print(mnumbers2)

result = np.vstack((mnumbers1, mnumbers2)) # matrisleri alt alta birleştirir. İkinci matrisi aldı ilk matrisin altına ekledi (v -> vertical)
result = np.hstack((mnumbers1, mnumbers2)) # matrisleri yan yana birleştirir. İlk matrisi aldı ikinci matrisin yanına ekledi (h -> horizontal)

result = numbers1 >= 50 # Çıktı: [False  True False  True False  True] her elemanı karşılaştırır
result = numbers1 % 2 == 0 # Çıktı: [ True False  True  True  True False] her elemanı karşılaştırır

print(numbers1[result]) # Çift olanları sorgulamıştık yukarıda ve burada da çift olanları dizi içinde yazdırdık
print(result)