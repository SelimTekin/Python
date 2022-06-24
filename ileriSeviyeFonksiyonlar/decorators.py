# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello", name)    # name parametresi, wrapper() ve func() fonksiyonlarında parametre olarak bulunmazsa hata verir

# sayHello("Selim")

# # selim = my_decorator(sayHello)
# # selim()

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1) # Fonksiyon 1 saniye bekler vew çalışmaya devam eder
        func(*args, **kwargs)
        finish = time.time()
        print("Fonksiyon " + func.__name__ + " " +  str(finish - start) + " saniye sürdü.")

    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)