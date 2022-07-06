import pandas as pd
import numpy as np

personeller = {
    'Çalışan':  ['Ahmet YIlmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları','Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları'],
    'Yaş': [30, 25, 45, 50, 23, 34, 42],
    'Semt': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
    'Maaş': [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups # Nasıl gruplandığı yazar. Çıktı: {'Bilgi İşlem': [1, 4], 'Muhasebe': [2, 5], 'İnsan Kaynakları': [0, 3, 6]}
result = df.groupby(["Departman", "Semt"]).groups # Çıktı: {('Bilgi İşlem', 'Maltepe'): [4], ('Bilgi İşlem', 'Tuzla'): [1], ('Muhasebe', 'Maltepe'): [2], ('Muhasebe', 'Tuzla'): [5], ('İnsan Kaynakları', 'Kadıköy'): [0, 6], ('İnsan Kaynakları', 'Tuzla'): [3]}

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy") # Sadece Kadıköy olanlar gruplanır
result = df.groupby("Departman").get_group("Muhasebe") # Sadece Muhasebe olanlar gruplanır
result = df.groupby("Departman").sum() # Yaş ve maaş toplamları yazar grup halinde
result = df.groupby("Departman").mean() # Yaş ve maaş ortalamaları yazar grup halinde
result = df.groupby("Departman")["Maaş"].mean() # Gruplanan departmanların maaş ortalaması
result = df.groupby("Semt")["Yaş"].mean() # Gruplanan semtlerin yaş ortalaması
result = df.groupby("Semt")["Maaş"].mean() # Gruplanan semtlerin maaş ortalaması
result = df.groupby("Semt")["Çalışan"].count() # Semtlere göre çalışan sayısı
result = df.groupby("Departman")["Yaş"].max() # Her departmanda maksimum yaşlar
result = df.groupby("Departman")["Maaş"].min() # Her departmanda minimum maaşlar
result = df.groupby("Departman")["Maaş"].max() # Her departmanda max maaşlar
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"] # Muhasebe departmanında max maaş
result = df.groupby("Departman").agg(np.mean) # Gruplanan departmanların numpy ile yaş ve maaş ortalamaları agg -> aggregation
result = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["Muhasebe"] # Muhasebenin toplam, ortalama, max ve min

print(result)