# Bellekte yer işgal etmeyen bir iterator üretir. (Sadece ekranda gösterme amaçlı)

# def cube():
#     for i in range(5):
#         yield i**3

# iterator = cube()
# iterator = iter(generator) # generator zaten iterator olan objeyi iteratorde kendi içinde çeviriyor. Yani buna ihtiyaç yok

# print(next(iterator)) # 0
# print(next(iterator)) # 1
# print(next(iterator)) # 8
# print(next(iterator)) # 27
# print(next(iterator)) # 64
# print(next(iterator)) # StopIteration error

# for i in cube():
#     print(i)

generator = (i**3 for i in range(5))
print(generator) # adresini yazar

for i in generator:
    print(i)

# print(next(generator)) # 0
# print(next(generator)) # 1
# print(next(generator)) # 8

# ------------------- Normalde kullandığımız -------------------
# def cube():
#     result = []

#     for i in range(5): # Yüksek bir sayı olsaydı belleği işgal edecekti.
#         result.append(i**3)
#     return result

# print(cube())