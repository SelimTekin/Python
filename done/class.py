# # class

# class Person:
#     # pass # Yer tutucu (bu olmasaydı hata verirdi çünkü class'ın içinde henüz metot veya attribute yok.)(if için de geçerli)

#     # class attributes
#     address = 'no information'  # Her zaman kulanılmayacak bilgiler
#     # constructor (yapıcı metot)
#     def __init__(self, name, year): # self oluşturulacak olan objeleri temsil ediyor o yüzden bu parametreye değer belirtmemiz gerekmiyor.init metodu class oluşturulduğunda çalıştırılır.
#         # object attributes # mutlaka tanımlanmasını istediğimiz bilgiler
#         self.name = name
#         self.year = year
#         print('init metodu çalıştı')

#     # instance methods

#     def intro(self):
#         print('Hello There. I am ' + self.name)
    
#     def calculateAge(self):
#         return 2022 - self.year
# # object(instance)

# p1 = Person(name = 'Selim', year = 2002) # böyle de olabilir. Okunabilirliği daha iyi
# p2 = Person(name = 'Tekin', year =  2003)

# p1.intro()
# p2.intro()

# print(f'adım: {p1.name} yaşım: {p1.calculateAge()}')
# print(f'adım: {p2.name} yaşım: {p2.calculateAge()}')
# uppdating

# p1.name = 'Ahmet'
# p1.address = 'İstanbul'

# #accessing object attributes

# print(f'p1 name: {p1.name} year: {p1.year} address: {p1.address}')
# print(f'p2 name: {p2.name} year: {p2.year} address: {p2.address}')

# print(p1) # Çıktı adres olur ve Person tipinde olduğunu söyler
# print(p2)


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle() # parametre belirtmezsek yaricap = 1
c2 = Circle(5)

print(f'c1: alan={c1.alan_hesapla()} çevre={c1.cevre_hesapla()}')
print(f'c2: alan={c2.alan_hesapla()} çevre={c2.cevre_hesapla()}')