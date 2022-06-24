# name = 'Selim Tekin'

# for letter in name:
#     if letter == 'e':
#         break
#     print(letter) # Çıktı: S # e harfini görünce döngüyü kırar

# for letter in name:
#     if letter == 'e':
#         continue
#     print(letter) # Çıktı: S l i m T k in (alt alta) # e harfini görünce o adımı atlayıp diğerinden devam eder

# ----------- Kasten yanlış yazılmış kod -----------
# x = 0
# while x < 5:
#     if x == 2:
#         continue # x, aşağı inemeyip x'i 1 arttıramaz bu yüzden 2'de takılı kalacağı için başa döner (Çıktı: 0 1) 
#                  #dolayısıyla x += 1 satırını if'in üstüne yazmamız lazım (bir alttaki kod bloğu)
#     print(x)
#     x += 1
# ----------------------------------------------------

# x = 0

# while x < 5:
#     x += 1
#     if x == 2:
#         continue # Doğru kod yazımı
#     print(x)

x = result = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x

print(f'0-100 arasındaki çift sayıların toplamı: {result}')