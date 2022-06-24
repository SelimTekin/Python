x = 6
hak = 5
devam = 'e'

result = 5 < x < 10

# and

result = 5 < x and x < 10 # True, True => True  True, False => False
result = hak > 0 and devam == 'e'

# or

result = (x > 0) or (x % 2 == 0) # True, False => True  True, True => True  False, False => False

# not

result = not(x > 0) # False

print(result)