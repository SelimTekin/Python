# Yöntem 1

import math
import math as islem

# value = dir(math) # moduldeki matematiksel işlemleri sıralar
# value = help(math) # işlemler hakkında bilgi verir
# value = help(math.factorial) # faktöriyel hakkında bilgi verir

# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5) # aşağı yuvarlama
# value = math.ceil(5) # yukarı yuvarlama

# value = islem.factorial(5)

# Yöntem 2

# def sqrt(x):            # fonksiyon burada olursa(importtan önce) value sonucu 3.0 olur
#     print('x: ' + x)

# from math import *
from math import factorial,sqrt,ceil

def sqrt(x):            # fonksiyon burada olursa(importtan sonra) value sonucu 9 olur (yani en son hangi fonksiyon varsa o kullanılır)
    print('x: ' + str(x))
# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)

print(value)