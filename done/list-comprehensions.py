# numbers = [x**2 for x in range(10)] # 0'dan 10'a kadar değerleri x'e atıyoruz(en soldaki) ve x'e gelen değere dizinin içindeki elemanları temsil ediyor
# print(numbers)

# numbers = []

# for x in range(10):
#     numbers.append(x)
# print(numbers)

# numbers = [x*x for x in range(10) if x%3==0]
# print(numbers)


# myString = 'Hello'
# myList = []

# for letter in myString:
#     myList.append(letter)
# print(myList)

# myList = [letter for letter in myString]
# print(myList)

# years = [1983, 1999, 2008, 1956, 1986]
# ages = [2022-year for year in years]
# print(ages)

# results = [x if x%2==0 else 'TEK' for x in range(1,10)]
# print(results)

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers =[(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)