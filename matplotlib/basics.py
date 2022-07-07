import matplotlib.pyplot as plt
import numpy as np

"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# matplotlib plot style sitesine bak
plt.plot(x, y, color="red", linewidth="5") # yukarıdaki x ve y listeleri. color çizgi rengi. linewidth çizgi kalınlığı
plt.plot(x, y, "-g") # Düz yeşil çizgi "-" -> stil "g" -> renk
plt.plot(x, y, "--g") # Çizgi çizgi şeklinde(dotted) yeşil bir çizgi "--" -> stil "g" -> renk
plt.plot(x, y, "o--r") # Çizgi çizgi şeklinde(dotted) yeşil bir çizgi "o" -> marker(her noktanın işaretle gösterimi) "--" -> stil "g" -> renk

plt.axis([0, 6, 0, 20]) # 0 ve 6 x'in başlangıç ve bitiş noktaları oluyor, 0 ve 20 ise y'nin. Yani x ve y eksenleri genişledi.

plt.title("Grafik Başlığı")
plt.xlabel("x label") # x ekseni adı
plt.ylabel("y label") # y ekseni adı

"""

"""
x = np.linspace(0, 2, 100) # linespace -> 0 ile 2 arasında 100 eşit parçaya böler

plt .plot(x, x, label="linear", color="red") # label -> çizginin adı
plt .plot(x, x**2, label="quadratic", color="yellow")                   # Tek bir grafik ile 3 tane çizgi
plt .plot(x, x**3, label="cubic", color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Simple Plot")

plt.legend() # labellar ile verdiğimiz değerler ekranda gösterilir

plt.show()

"""

"""
x = np.linspace(0, 2, 100) # linespace -> 0 ile 2 arasında 100 eşit parçaya böler

fig, axs = plt.subplots(3) # alt alta 3 tane grafik oluşturmak için yaptık (fig örneği altta)

axs[0].plot(x, x, color="red") # 1. grafik
axs[0].set_title("linear")

axs[1].plot(x, x**2, color="green") # 2. grafik
axs[1].set_title("quadratic")

axs[2].plot(x, x**3, color="yellow") # 3. grafik
axs[2].set_title("cubic")

plt.tight_layout() # layout türünü değiştirdik. Bunu yapmazsak grafikler ile grafik başlıkları iç içe geçer.

plt.show()

"""
"""

x = np.linspace(0, 2, 100) # linespace -> 0 ile 2 arasında 100 eşit parçaya böler

fig, axs = plt.subplots(2,2) # 2'ye 2'lik grafik oluşturmak için yaptık
fig.suptitle("Grafik Başlığı")

axs[0,0].plot(x, x, color="red") # 0. satır 0. sütun (yani sol üstte görünür grafik)
axs[0,1].plot(x, x**2, color="blue") # (sağ üst)
axs[1,0].plot(x, x**3, color="green") # (sol alt)
axs[1,1].plot(x, x**4, color="yellow") # (sağ alt)

"""

import pandas as pd
# df = pd.read_csv("../pandas/datasets/nba.csv")
# print(df.columns)
df = pd.read_csv("../pandas/datasets/nba.csv")
# df = df.drop(["draft_number"], axis=1).groupby("team_abbreviation").mean() #draft_number isimli kolonu sildik. (axis=1 kolon olduğunu belirtmek için)
df = df.groupby("team_abbreviation")[["gp", "age", "player_weight"]].mean()

df.head().plot(subplots=True) # subplot=True olmazsa tek bir grafikte 3 çizgi gösteriyor olursa 3 grafikte ayrı ayrı gösteriyor.
# df.head().plot()
plt.legend()
plt.show()