# global scope

# x = 'global x'

# def function():
#     # local scope
#     x = 'local x'
#     print(x) 

# function() # Çıktı: local x
# print(x) # Çıktı: global x

# --------------------------------

# name = 'Selim'

# def changeName(newName):
#     name = newName
#     print(name)

# changeName('Tekin')
# print(name)

# --------------------------------

# name = 'global string'

# def greeting():
#     name = 'Selim'

#     def hello():
#         print('Hello ' + name) # name Selim olur. Basamak çıkar gibi hangisinde name'i bulursa onu alır
    
#     hello()

# greeting()

# --------------------------------

from re import X


x = 50

def test():
    global x # dışardaki x'i temsil eder
    print(f'x: {x}')

    x = 100
    print(f'changed x to {x}')

test() # Çıktı: 50 ve changed x to 100
print(x) # Çıktı: 100