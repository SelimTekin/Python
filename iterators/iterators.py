liste = [1, 2, 3, 4, 5]

# for i in liste:
#     print(i)

# print(dir(liste)) # __iter__ metoduna sahip yani iterable obje

# iterator  = iter(liste)
# print(iterator) # iterator'ın adresini yazar

# print(next(iterator)) # listenin elemanları tek tek gelecek(Arda arda çağırılırsa) Çıktı: 1
# print(next(iterator)) # listenin elemanları tek tek gelecek Çıktı: 2
# print(next(iterator)) # listenin elemanları tek tek gelecek Çıktı: 3
# print(next(iterator)) # listenin elemanları tek tek gelecek Çıktı: 4
# print(next(iterator)) # listenin elemanları tek tek gelecek Çıktı: 5
# print(next(iterator)) # 6. eleman yok. StopIteration hatası verir

# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)                           # for döngüsünün arka planı
#     except StopIteration:
#         break


class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else: 
            raise StopIteration

list = MyNumbers(10,20)

myiter = iter(list)

# print(next(myiter)) # 10
# print(next(myiter)) # 11

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break

# for x in list:
#     print(x)