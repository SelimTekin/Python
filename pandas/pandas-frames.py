import pandas as pd

list = [["Ali",50], ["Ahmet",60], ["Yağmur",70], ["Çınar",80]]
dict = {"Name":["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade":[50, 60, 70, 80]}
dict_list = [
    {"Name": "Ahmet", "Grade":50},      # Satırları temsil ediyor her biri
    {"Name": "Ali", "Grade":60},
    {"Name": "Yağmur", "Grade":70},
    {"Name": "Çınar", "Grade":80}
]

df = pd.DataFrame()
# Çıktı:  Empty DataFrame
        # Columns: []
        # Index: []

df = pd.DataFrame([1, 2, 3, 4])
# Çıktı:     0 -> kolon adı vermediğimiz için kolon numarası 0 olarak yazıyor
        # 0  1
        # 1  2
        # 2  3
        # 3  4

df = pd.DataFrame(list, index = [1, 2, 3, 4], columns = ['Name', 'Grade'], dtype = float)
# Çıktı:       Name   Grade
        # 0     Ali      50.0
        # 1   Ahmet      60.0
        # 2  Yağmur      70.0
        # 3   Çınar      80.0

df = pd.DataFrame(dict, index = ["1200", "50", "50", "24"]) # Aynı sadece indekslerin yerinde öğrenci nolar yazıyor
df = pd.DataFrame(dict_list) # aynı
df = pd.DataFrame(dict_list, index = ["1200", "50", "50", "24"]) # aynı
print(df)

# s1 = pd.Series([3, 2, 0, 1])
# s2 = pd.Series([0, 3, 7, 2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)
# # Çıktı:     apples  oranges -> kolon adları
#         # 0       3        0
#         # 1       2        3                 #Bu bir dataFrame
#         # 2       0        7
#         # 3       1        2


# print(df)