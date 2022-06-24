# message = 'Hello there. My name is Selim'.split()

# # myList = [1,2,3]
# # myList = ['bir',2,True,5.6]
# # print(myList)

# list1 = ['one','two','three']
# list2 = ['four','five','six']
# numbers = list1 + list2
# print(numbers)
# print(len(numbers))
# print(message[0])

# userA = ['Selim',19]
# userB = ['Tekin',20]

# users = [userA,userB] # userA ve userB elemanlarına sahip 2 elemanlı bir dizi

# print(users) # Çıktı: [[Selim,19], [Tekin,20]]
# print(users[0][0]) # Çıktı: Selim

arabalar = ['BMW','Mercedes','Opel','Mazda']

result = 'Opel' in arabalar
arabalar[-2:] = ['Toyota','Renault'] # Listenin son iki elemanı değişti
result = arabalar
result = arabalar + ['Audi','Nissan'] # arabalar listesi üzerine ekleme yapıldı (arabalar listesi hala 4 elmanlıdır. Farklı bir liste oluşturup içine atılabilir, burada mesela result listesini atadık son halini)
del arabalar[-1] # son eleman silindi
result = arabalar
result = arabalar[::-1] # liste elemanları tersten yazıldı

print(result)