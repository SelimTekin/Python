import pandas as pd
import numpy as np

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 13, 20, 25],
    "Column3": ["abc", "bcaa", "ade", "cb", "dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x * x

result = df
result = df["Column2"].unique() # Çıktı: [10 20 13 25] (tekrarlamayan alanları getirir)
result = df["Column2"].nunique() # Çıktı: 4 (tekrarlamayan alanların kaç tane olduğunu söyler)
result = df["Column2"].value_counts() # her elemandan kaç tane olduğunu söyler
result = df["Column1"] * 2 # Her eleman 2 ile çarpılır
result = df["Column1"].apply(kareal) # aynısını burada apply metodunun içine yazdığımız fonksiyonla yaptık
result = df["Column1"].apply(kareal2) # aynı
result = df["Column1"].apply(lambda x: x * x) # aynı
df["Column4"] = df["Column3"].apply(len) # kolon3'teki her bir elemanın uzunluklarını yazar
# print(df)
result = df.columns
result = len(df.columns) # kaç kolon olduğu yazar
result = df.index # Çıktı: RangeIndex(start=0, stop=5, step=1)
result = len(df.index) # kaç index olduğu yazar
result = df.info # df hakkında bilgi verir (satır ve kolonları da yazar)

result = df.sort_values("Column2") # sayıların sırasına göre yazılır # varsayılan artan (ascending = True)
result = df.sort_values("Column3") # alfabetik sıralanır
result = df.sort_values("Column3", ascending = False) # azalan sıralanır

data = {
    "Ay": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan"],
    "Kategori": ["Elektronik", "Elektronik", "Elektronik", "Kitap", "Kitap", "Kitap", "Giyim", "Giyim", "Giyim"],
    "Gelir": [20, 30, 15, 14, 32, 42, 12, 36, 52]
}
df = pd.DataFrame(data)
print(df.pivot_table(index = "Ay", columns = "Kategori", values = "Gelir"))
# Çıktı:  Kategori  Elektronik  Giyim  Kitap
        # Ay
        # Haziran           30     36     32
        # Mayıs             20     12     14
        # Nisan             15     52     42