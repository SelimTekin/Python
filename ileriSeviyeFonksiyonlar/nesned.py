# def greeting(name):
#     print("hello", name)

# print(greeting('Selim'))
# print(greeting) # adres döner

# sayHello = greeting

# print(sayHello)
# print(greeting) # yukardakiyle aynı adres döner. Çünkü verinin bulunduğu konum değil adres bilgisi aynıdır.

# del sayHello
# print(sayHello) # NAmeError hatası
# print(greeting) # greeting hala duruyor


# encapsulation

# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)


# outer(10)
# inner_increment(10) # NameError tanımlanmayan değer hatası verir (outer kapsamında çalıştırılacak olan değer)


from typing import Type


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")

    if not number >= 0:
        raise ValueError("Number must be zero or positive")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)

    return inner_factorial(number)
try:
    print(factorial(4)) # parametre olmazsa except bloğu çalışır. Çıkıt: factorial() missing 1 required positional argument: 'number'
except Exception as ex:
    print(ex)