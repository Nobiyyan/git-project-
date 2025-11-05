import numpy as np

nilai = np.array([90,91,85,80,78,71,64,67,83,88,
                  62,56,100,98,70,60,56,40,30,20,
                  99,45,44,38,90,94,10,11,23,45])

sorted_nilai = np.sort(nilai)[::-1]
print("Urutan nilai dari yang terbesar adalah", np.sort(nilai)[::-1])
print("5 Nilai terbesar adalah ", sorted_nilai[0:5])
