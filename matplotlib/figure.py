import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 9, 20)
y = x ** 3
z = x ** 2
"""

figure = plt.figure()

# axes = figure.add_axes([0.2, 0.2, 0.8, 0.8]) # 0,2'ler sırayla soldan ve alttan %20 uzaklıkta 0.8'ler ise genişlik ve yükseklik %80 kaplar
axes_cube = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes_cube.plot(x, y, 'b') # 'b' mavi rengi temsil ediyor.
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15, 0.6, 0.25, 0.25])
axes_square.plot(x, z, 'r') # 'b' mavi rengi temsil ediyor.
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")

"""

"""

figure = plt.figure()

axes = figure.add_axes([0, 0, 1, 1])

axes.plot(x, y, label="Square")
axes.plot(x, z, label="Cube")
axes.legend(loc=1) # loc legend'ın konumunu belirler. 1->sağ üst, 2->sol üst, 3->sol alt, 4->sağ alt  loc -> location

"""

fig, axes = plt.subplots(nrows=2,ncols=1, figsize=(8, 8)) # 2 satır 1 sütun figsize(8, 8) figure'ün boyutu(figürü kaydedersek bu boyutta kaydolur)

axes[0].plot(x, y)
axes[0].set_title("Cube")
axes[1].plot(x, z)
axes[1].set_title("Square")

plt.tight_layout() # birbirine girmesin diye

# fig.savefig("figure1.png")
fig.savefig("figure2.pdf")

plt.show()