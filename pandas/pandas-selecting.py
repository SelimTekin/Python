import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3), index = ["A", "B","C"], columns = ["Column1", "Column2", "Column3"]) # randn -> 0-1 arası sayı üretir negaif dahil

result = df
result = df["Column1"]
result = type(df["Column1"]) # <class 'pandas.core.series.Series'>
result = df[["Column1", "Column2"]] # Bunları liste halinde gönderdik göründüğü gibi (en dışta bir tane daha köşeli parantez var)

# loc["row", "column"] | loc["row"] | loc[:, "column"]
result = df.loc["A"]      # loc -> location
# Çıktı:  Column1    0.592381
        # Column2   -1.282077
        # Column3    0.405735
        # Name: A, dtype: float64

result = type(df.loc["A"]) # <class 'pandas.core.series.Series'>
result = df.iloc[2]["Column1"] # 2. satır gelir. İndekslerimiz A,B ve C olmasına rağmen indeksle çağırmak istiyosak bu şekilde. (iloc -> indexlocation)
# result = df.loc[:, "Column1"]   # Sadece kolon 1
# result = df.loc[:, ["Column1", "Column2"]]      # Kolon 1 ve kolon 2
# result = df.loc[:, "Column1":"Column2"]      # Kolon 1 ve kolon 2 arası gelir (başlangıç ve bitiş dahil)
# result = df.loc[:, :"Column2"]      # Başlangıçtan kolon 2'ye kadar gelir (başlangıç ve bitiş dahil)
# result = df.loc["A":"B", :"Column2"]      # A-B arası kolon 2'ye kadar gelir (başlangıç ve bitiş dahil)
# result = df.loc[:"B", :"Column2"]      # Başlangıçtan B'ye kadar kolon 2'ye kadar gelir (başlangıç ve bitiş dahil)
# result = df.loc["A", "Column2"] # Çıktı: 0.4616287037596513 (tek bir değer gelir)
# result = df.loc[["A", "B"], ["Column1","Column2"]] # A ve B satırlarındaki kolon 1 ve kolon 2 gelir.

# df["Column4"] = pd.Series(randn(3), ["A", "B", "C"]) # Yeni bir kolon oluşturduk (yeni bir seri gibi)
# df["Column5"] = df["Column1"] + df["Column3"] # kolon 1 ve 3'ün toplamı olan yeni bir kolon 5 oluşturduk

# # print(df.drop("Column5", axis=1)) # kolon 5'i sildik ancak orijinal seride değişiklik olmadı (orijinal seride kolon 5 var hala)

# # result = df.drop("Column5", axis=1, inplace=True) # inplace=True ile orijinal seriyi de güncellemiş olduk
# result = df.drop("Column5", axis=1, inplace=False) # inplace=False ile orijinal seride değişiklik olmadı
print(result)
print(df)
