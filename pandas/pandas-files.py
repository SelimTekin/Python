import pandas as pd
# import sqlite3      # pip install sqlite3        # ileriki konular

df = pd.read_csv("max_planck_weather_ts.csv")   # Çok fazla veri olduğu için ilk ve son 5 satırı gösterdi (aradakilere ... yazdı)
df = pd.read_json("sample.json", encoding="utf-8")
df = pd.read_excel("sample.xlsx")       # pip install openpyxl (indirmen lazım) ve içindekileri güncellemen için excel uygulamasını indirip oradan güncellemen lazım yoksa güncellenmiyor eski hali geliyor.
# Çıktı:
#      Name  Grade
# 0   Selim    100
# 1   Tekin     90
# 2    Enes    100
# 3  Dönmez     90


# connection = sqlite3.connect("sample.db")
# df = pd.read_sql_query("SELECT * FROM students", connection)          # ileriki konular
print(df)