import numpy as np

dataUang = np.array([10,30,20,23,12,34,11,40,50,60,45,35])

print("Rata-rata:", dataUang.mean())
untung_min = dataUang.min()
untung_maks = dataUang.max()

for i in range(len(dataUang)):
    if dataUang[i] == untung_min:
        print("Keuntungan terendah:", untung_min, "pada hari ke", i + 1)

for i in range(len(dataUang)):
    if dataUang[i] == untung_maks:
        print("Keuntungan tertinggi:", untung_maks, "pada hari ke", i + 1)
