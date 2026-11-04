# Monitoring Kualitas Sinyal / SNR
Kelompok B - Telekomunikasi
Nama: Davina Almira Alexandra
NIM: 03041282631056
Kelas: B - Palembang
---

## 1. Deskripsi Program
Program ini mengklasifikasikan kualitas sinyal berdasarkan nilai SNR (*Signal-to-Noise Ratio*) dalam satuan dB. Setiap data diberi status (RENDAH, BAIK, atau SANGAT BAIK), kemudian program menampilkan jumlah data tiap kategori serta ringkasan statistik berupa rata-rata, persentase kategori, nilai maksimum, dan nilai minimum. Program hanya menggunakan library standar Python (`math`), sehingga tidak memerlukan instalasi tambahan.

## 2. Cara Menjalankan
Pastikan Python 3 sudah terpasang, lalu jalankan perintah berikut di folder yang berisi `main.py`:
```python main.py```

## 3. Aturan Status
| Rentang SNR          | Status      |
|----------------------|-------------|
| SNR < 10 dB          | RENDAH      |
| 10 ≤ SNR < 20 dB     | BAIK        |
| SNR ≥ 20 dB          | SANGAT BAIK |

## 4. Data yang Digunakan
Total data yang diproses adalah 20 data, terdiri dari 15 data inti dan 5 data tambahan.

Data inti:
`[5, 8, 11, 14, 18, 22, 27, 9, 16, 24, 12, 30, 7, 20, 15]`

Data tambahan (5 data):
`[0, 3, 10, 19, 35]`

### 4.1 Alasan Pemilihan Data Tambahan
Lima data tambahan dipilih untuk menguji batas kategori dan memperluas variasi nilai. Data inti sudah mencakup nilai 7 sampai 30 dB, sehingga data tambahan difokuskan pada tiga hal: pasangan nilai di sekitar batas kategori, nilai ekstrem bawah dan atas, dan nilai yang belum terwakili.

| Nilai (dB) | Status      | Alasan pemilihan |
|------------|-------------|------------------|
| 0          | RENDAH      | Menguji batas bawah rentang. Data inti belum memiliki nilai di bawah 5 dB. |
| 3          | RENDAH      | Menambah variasi di kategori RENDAH yang sebelumnya hanya berisi nilai 5 sampai 9 dB. |
| 10         | BAIK        | Menguji batas bawah kategori BAIK. Bersama nilai 9 pada data inti, program diuji untuk membedakan 9 (RENDAH) dan 10 (BAIK). |
| 19         | BAIK        | Menguji batas atas kategori BAIK. Bersama nilai 20 pada data inti, program diuji untuk membedakan 19 (BAIK) dan 20 (SANGAT BAIK). |
| 35         | SANGAT BAIK | Memperluas nilai maksimum di atas data inti (30 dB), sehingga rentang data menjadi lebih lebar. |

### 4.2 Kewajaran Nilai yang Dipilih
Semua nilai tambahan berada dalam rentang yang wajar untuk pengukuran SNR pada sistem komunikasi nyata:
- **0 dB** berarti daya sinyal sama dengan daya noise. Kondisi ini wajar terjadi ketika sinyal sangat lemah, misalnya di tepi jangkauan atau saat ada interferensi berat.
- **3 dB** berarti sinyal hanya sedikit di atas noise. Kondisi ini masih mungkin terjadi pada koneksi yang hampir terputus.
- **10 dB** dan **19 dB** adalah nilai yang umum muncul pada kondisi sinyal menengah. Keduanya dipilih karena berada tepat di sisi batas kategori.
- **35 dB** adalah nilai yang wajar untuk sinyal kuat, misalnya saat perangkat berada dekat dengan pemancar seperti BTS atau access point.
Tidak ada nilai yang bersifat tidak wajar secara fisik, dan semua nilai berada dalam satuan dB yang sama dengan data inti.

## 5. Penjelasan Fungsi
| Fungsi | Tugas | Keterangan |
|--------|-------|------------|
| `kualitas_sinyal(snr)` | Menentukan status kualitas sinyal | Menggunakan `if/elif/else`. Mengembalikan (`return`) string status. |
| `hitung_kategori(data)` | Menghitung jumlah data tiap kategori | Menggunakan `for` untuk memproses seluruh data. Mengembalikan dictionary berisi jumlah tiap kategori. |
| `rata_rata(data)` | Menghitung rata-rata | Perhitungan numerik `sum(data) / len(data)`. Mengembalikan nilai rata-rata. |
| `main()` | Menampilkan tabel data dan ringkasan | Menggunakan `for` untuk mencetak setiap data beserta status dan sumbernya. |

### 5.1 Fungsi Tambahan: `hitung_persentase(jumlah, total)`
Menghitung persentase setiap kategori terhadap total data.

Parameter jumlah: dictionary hasil hitung_kategori, berisi jumlah data tiap kategori.
Parameter total: banyaknya seluruh data yang diproses, yaitu 20.
Nilai kembali: dictionary berisi persentase tiap kategori, dengan pembulatan dilakukan saat ditampilkan (satu angka di belakang koma).
Rumus: persentase = jumlah_kategori / total × 100.

Di dalam main(), fungsi ini dipanggil pada bagian ringkasan, lalu hasilnya ditampilkan di samping jumlah tiap kategori.

## 6. Hasil Test
```
===== TEST kualitas_sinyal(snr) =====
| Input (dB) | Expected     | Actual       | Hasil |
| 0          | RENDAH       | RENDAH       | PASS |
| 10         | BAIK         | BAIK         | PASS |
| 11         | BAIK         | BAIK         | PASS |
| 18         | BAIK         | BAIK         | PASS |
| 19         | BAIK         | BAIK         | PASS |
| 22         | SANGAT BAIK  | SANGAT BAIK  | PASS |
| 27         | SANGAT BAIK  | SANGAT BAIK  | PASS |
| 35         | SANGAT BAIK  | SANGAT BAIK  | PASS |
```
Hasil pengujian `kualitas_sinyal` menunjukkan bahwa seluruh 8 `DATA_UJI` menghasilkan status yang sesuai harapan (8 PASS dari 8). Dengan demikian, fungsi ini sudah menerapkan aturan status dengan benar untuk nilai-nilai tersebut. Input pada tabel ini saya ambil dari `DATA_SNR`.

## 7. Hasil Eksekusi
```
====================================================
MONITORING KUALITAS SINYAL / SNR
====================================================
No    SNR (dB)   Status      Sumber
1            5   RENDAH      Inti
2            8   RENDAH      Inti
3           11   BAIK        Inti
4           14   BAIK        Inti
5           18   BAIK        Inti
6           22   SANGAT BAIK Inti
7           27   SANGAT BAIK Inti
8            9   RENDAH      Inti
9           16   BAIK        Inti
10          24   SANGAT BAIK Inti
11          12   BAIK        Inti
12          30   SANGAT BAIK Inti
13           7   RENDAH      Inti
14          20   SANGAT BAIK Inti
15          15   BAIK        Inti
16           0   RENDAH      Tambahan
17           3   RENDAH      Tambahan
18          10   BAIK        Tambahan
19          19   BAIK        Tambahan
20          35   SANGAT BAIK Tambahan

====================================================
RINGKASAN
====================================================
Jumlah RENDAH      : 6 data (30.0%)
Jumlah BAIK        : 8 data (40.0%)
Jumlah SANGAT BAIK : 6 data (30.0%)
Rata-rata SNR          : 15.25 dB
Nilai maksimum         : 35 dB
Nilai minimum          : 0 dB
```

### Interpretasi Singkat
Dari 20 data, 6 data (30,0%) berada pada kategori RENDAH, 8 data (40,0%) pada kategori BAIK, dan 6 data (30,0%) pada kategori SANGAT BAIK. Rata-rata SNR sebesar 15,25 dB berada di kategori BAIK. 