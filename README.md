# 🧮 Tugas Dasar Pemrograman – Studi Kasus dengan NumPy

Repository ini berisi program sederhana menggunakan **Python** dan **library NumPy** untuk menyelesaikan beberapa studi kasus dasar dalam pengolahan data menggunakan array.  
Seluruh data yang digunakan merupakan **data dummy (simulasi)** yang dibuat untuk keperluan pembelajaran.

---

## 📘 **Daftar Studi Kasus**

### **1️⃣ Konversi Suhu dari Celcius ke Fahrenheit**
**Deskripsi Kasus:**  
Seorang ilmuwan memiliki data suhu di Singapura selama 10 hari terakhir yang disimpan dalam sebuah array. Suhu tersebut ingin dikonversi dari Celcius menjadi Fahrenheit.

**Tujuan:**  
Menampilkan suhu awal dalam Celcius dan hasil konversinya ke Fahrenheit menggunakan library NumPy.

**Rumus:**  
\[
F = \frac{9}{5} \times C + 32
\]

**Langkah Utama:**
- Membuat array NumPy berisi data suhu 10 hari (dalam Celcius).  
- Melakukan konversi ke Fahrenheit dengan operasi vektor NumPy.  
- Menampilkan hasilnya ke layar.

---

### **2️⃣ Pengurutan Nilai Ujian Siswa**
**Deskripsi Kasus:**  
Seorang guru Matematika memiliki data nilai ujian sebanyak 30 siswa. Nilai tersebut ingin disimpan dalam array, kemudian diurutkan dari nilai tertinggi ke terendah. Guru juga ingin melihat 5 nilai tertinggi saja.

**Tujuan:**  
Menampilkan seluruh nilai yang telah diurutkan serta menampilkan 5 nilai tertinggi.

**Langkah Utama:**
- Membuat array NumPy berisi 30 nilai dummy siswa.  
- Mengurutkan array menggunakan `np.sort()` atau `[::-1]`.  
- Menampilkan seluruh nilai dan 5 nilai tertinggi.

---

### **3️⃣ Analisis Keuntungan Harian Toko Online**
**Deskripsi Kasus:**  
Seorang analis keuangan memiliki data keuntungan harian toko online selama 14 hari terakhir. Data disimpan dalam array NumPy untuk memudahkan analisis.

**Tujuan:**  
Mengetahui rata-rata keuntungan per hari, nilai keuntungan tertinggi, nilai keuntungan terendah, dan hari ke berapa masing-masing nilai tersebut terjadi.

**Langkah Utama:**
- Membuat array NumPy berisi 14 data dummy keuntungan harian.  
- Menghitung rata-rata menggunakan `np.mean()`.  
- Menemukan nilai maksimum dan minimum menggunakan `np.max()` dan `np.min()`.  
- Menemukan indeks (hari) dengan keuntungan tertinggi dan terendah menggunakan `np.argmax()` dan `np.argmin()`.

---

## ⚙️ **Library yang Digunakan**
- [NumPy](https://numpy.org/)  
  Digunakan untuk manipulasi array dan perhitungan numerik.

---

## 💻 **Cara Menjalankan Program**
1. Pastikan Python sudah terinstal di komputer.  
2. Instal library NumPy jika belum terpasang:
   ```bash
   pip install numpy
