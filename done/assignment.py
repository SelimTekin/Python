# x, y, z = 5, 10, 20
# x, y = y, x    # x = 10 y = 5

# y //= 5  # Tam bölme yapar y = y // 5

# values = 1, 2, 3

# print(values)
# print(type(values))

# x, y, z = values # 1, 2, 3

values = 1, 2, 3, 4, 5
x, y, *z = values # Çıktı: 1 2 [3, 4, 5]
x, *y, z = values # Çıktı: 1 [2, 3, 4] 5
print(x, y, z)