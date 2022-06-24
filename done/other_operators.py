# Identity Operator: is

# x = y = [1, 2, 3] # Aynı adresler
# z = [1, 2, 3] # Farklı adres

# print(x == y) # True
# print(x == z) # True çünkü değerlere bakar

# print(x is y) # Adreslere bakar. True döner çünkü aynı referansa sahip
# print(x is z) # Adreslere bakar. False döner çünkü değerleri aynı fakat farklı referanslara sahip

# x = [1, 2, 3]
# y = [2, 4]

# del x[2]
# y[1] = 1
# y.reverse()

# print(x == y) # True
# print(x is y) # False
# print(x is not y) # True

# Membership Operator: in

x = ['apple', 'banana']
print('apple' in x) # True

name = 'Selim'
print('e' in name) # True
print('e' not in name) # False