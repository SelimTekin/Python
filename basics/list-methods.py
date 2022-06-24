# numbers = [1,10,5,16,4,9,10]
# letters = ['a','g','s','b','y','a','s']

# val = min(numbers)
# val = max(numbers)
# val = min(letters) # a
# val = max(letters) # y

# numbers.append(39) # listenin sonuna 39 eklenir
# numbers.insert(3, 78) # 3. indexin önüne 78 eklenir sağdakiler kayar
# numbers.insert(-1, 59) # sonuncu indexin önüne 59 eklenir (-1 yerine len(numbers) da yazılabilir), sonuncu index hala sondadır

# numbers.pop() # sondaki elemani siler ( pop(-1) ile aynı )
# numbers.pop(0) # ilk elemani siler
# numbers.remove(16) # aradığı elemanı siler yani 39 rakamını siler

# numbers.sort() # listeyi sıralar
# numbers.reverse() # listeyi tersine sıralar
# letters.sort() # listeyi sıralar
# letters.reverse() # listeyi tersine sıralar

# print(numbers.count(10)) # kaç tane 10 var

# numbers.clear() # listenin tüm elemanlarını siler
# print(numbers, letters) 

markalar = [] # boş dizi oluşturduk

marka = input("marka: ")
markalar.append(marka) # girilen inputları markalar dizisine ekledik
print(markalar)