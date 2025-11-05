# listFactor = []
# def factor(n):
#     for i in range(1,n+1):
#         if n%i == 0:
#             listFactor.append(i)
#     print(f"Faktor dari {n} adalah {listFactor}")

# def jumlahDeret(x):
#     total = 0
#     for i in range(x+1):
#         total += i
#     return total

# def totalGanjil(num):
#     listGanjil = []
#     for i in range(num+1):
#         if i%2 == 1:
#             listGanjil.append(i)
#     return listGanjil

# inputAngka = int(input("Masukkan angka : "))
# factor(inputAngka)
# print("Total dari deret angka", inputAngka, "adalah", jumlahDeret(inputAngka))
# print("Angka ganjil dari angka", inputAngka, "adalah", totalGanjil(inputAngka))

def cek_prima(number):
    for i in range (2, number):
        if number%i == 0:
            return False
            break
    return True

def konversi_suhu(celcius):
    F = (9/5) * celcius + 32
    return F

def hitungVokal(kalimat):
    totalVokal = 0
    listVokal = ['a','i','u','e','o']
    for i in kalimat.lower():
        if i in listVokal:
            totalVokal += 1
    return totalVokal
        

num = int(input("Masukkan angka : "))
kalimat = input("Masukkan String : ")

print(cek_prima(num))
print("Konversi suhu dari", num, "celcius adalah", konversi_suhu(num), "Fahrenheit")
print("Jumlah huruf vokal dari string", kalimat, "adalah", hitungVokal(kalimat))




