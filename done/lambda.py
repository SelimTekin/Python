# def square(num): return num ** 2
square = lambda num: num ** 2 # isimsiz fonksiyon. Normal sfonksiyon olarak da kullanılabilir

numbers = [1, 3, 5, 9, 10, 4]

# result = list(map(lambda num: num ** 2, numbers))
# result = list(map(square, numbers)) # fonksiyon ve dizi adını parametre olarak verdik. numbers dizisini for ile tek tek dolaşacağımıza map ile yaptık

# for item in map(square, numbers):
#     print(item)

# def check_even(num): return num % 2 == 0
check_even = lambda num: num % 2 == 0

# result = list(filter(check_even, numbers))
# result = list(filter(lambda num: num % 2 == 0, numbers))
# result = list(filter(check_even, numbers))
result = check_even(numbers[2]) # Çıktı: False 4(index) yazsaydık True olurdu

print(result)