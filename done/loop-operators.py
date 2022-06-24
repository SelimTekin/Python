# range()
# for item in range(50,100,20): # 50'den başla 100'e 20 20 git
#     print(item)

# print(list(range(5,10,2))) # Çıktı: 5 7 9 liste şeklinde yazar

# enumerate()

# index = 0
# greeting = 'Hello'

# for index,letter in enumerate(greeting): # greeting stringini index ve value şeklinde oluşturur
#     print(f'index: {index} letter: {letter}')
#     index += 1

# for item in enumerate(greeting): # greeting stringini index ve value şeklinde oluşturur
#     print(item) # Çıktı: (0, 'H') (1, 'e') (2, 'l') (3, 'l') (4, 'o') alt alta

# # Alternatif

# for letter in greeting:
#     print(f'index: {index} letter: {greeting[index]}')
#     index += 1

# zip()

list1  = [1, 2, 3]
list2 = ['a', 'b', 'c'] # Ayrıca 'd' diye bir eleman daha olsaydı ona eşleşecek eleman kalmayacağı için çıktı yine aynı olurdu (yukardaki ve aşağıdaki için de geçerli)
list3 = [100, 200, 300, 400]

print(list(zip(list1, list2, list3))) # eşleştirme yapıldı Çıktı: [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

for item in zip(list1, list2, list3):
    print(item) #Çıktı aynı fakat alt alta yazılır

for a,b,c in zip(list1, list2, list3):
    print(a) # Çıktı: 1 2 3 fakat alt alta yazılır