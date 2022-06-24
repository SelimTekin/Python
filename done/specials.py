myList = [1,2,3]
myString = 'my String'

print(len(myList)) # 3
print(len(myString)) # 9
print(type(myList))
print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
                                            # Anladığım kadarıyla kütüphane içinde bulunan hazır metotların içeriğini değiştiriyoruz
    def __del__(self):
        print('film objesi silindi')

m = Movie('film adı', 'director', 120)

# print(str(myList))
print(str(m)) # Movie objesinin ram üzerinde hangi konumda olduğunu gösterirdi normalde AMA Movie class'ında str metodu yaptık. 
# del ile objeyi silmesek bile obje bi süre kullanılmadığında bellek üzerinden silinir
# print(len(myList))
# print(len(m))

# del m # film objesi silindi yazar 

# print(m) # Objenin tanımlı olmadığı hartası verir