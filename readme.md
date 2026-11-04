# Monitoring Kualitas Sinyal / SNR

**Kelompok B – Telekomunikasi**
**Nama:** Davina Almira Alexandra
**NIM:** 03041282631056

---

## 1. Deskripsi Program

Program ini mengklasifikasikan kualitas sinyal berdasarkan nilai SNR (*Signal-to-Noise Ratio*) dalam satuan dB. Setiap data diberi status (RENDAH, BAIK, atau SANGAT BAIK), kemudian program menampilkan jumlah data tiap kategori serta ringkasan statistik berupa rata-rata, simpang baku, nilai maksimum, dan nilai minimum.

Program hanya menggunakan library standar Python (`math`), sehingga tidak perlu instalasi tambahan.

## 2. Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan perintah berikut di folder yang berisi `main.py`:

```
python main.py
```

## 3. Aturan Status

| Rentang SNR          | Status      |
|----------------------|-------------|
| SNR < 10 dB          | RENDAH      |
| 10 ≤ SNR < 20 dB     | BAIK        |
| SNR ≥ 20 dB          | SANGAT BAIK |

## 4. Data yang Digunakan

Total data yang diproses adalah **20 data**, terdiri dari 15 data inti dan 5 data tambahan.

**Data inti (15 data, dipertahankan sesuai soal):**

`[5, 8, 11, 14, 18, 22, 27, 9, 16, 24, 12, 30, 7, 20, 15]`

**Data tambahan (5 data):**

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

Tidak ada nilai yang bersifat tidak mungkin secara fisik, dan semua nilai berada dalam satuan dB yang sama dengan data inti.

## 5. Penjelasan Fungsi

| Fungsi | Tugas | Keterangan |
|--------|-------|------------|
| `kualitas_sinyal(snr)` | Menentukan status kualitas sinyal | Menggunakan `if/elif/else`. Mengembalikan (`return`) string status. |
| `hitung_kategori(data)` | Menghitung jumlah data tiap kategori | Menggunakan `for` untuk memproses seluruh data. Mengembalikan dictionary berisi jumlah tiap kategori. |
| `rata_rata(data)` | Menghitung rata-rata | Perhitungan numerik `sum(data) / len(data)`. Mengembalikan nilai rata-rata. |
| `simpang_baku(data)` | Menghitung simpang baku sebagai ukuran variasi | Menggunakan rumus `σ = √( Σ(xᵢ − μ)² / N )` dengan `for`. Mengembalikan nilai simpang baku. |
| `main()` | Menampilkan tabel data dan ringkasan | Menggunakan `for` untuk mencetak setiap data beserta status dan sumbernya. |

## 6. Pemenuhan Ketentuan

| Ketentuan | Implementasi di `main.py` |
|-----------|---------------------------|
| List menyimpan 20 data | `DATA_SNR = DATA_INTI + DATA_TAMBAHAN` |
| Minimal 3 function dengan tugas berbeda | 4 function: `kualitas_sinyal`, `hitung_kategori`, `rata_rata`, `simpang_baku` |
| Decision `if/elif/else` | Dalam fungsi `kualitas_sinyal` |
| Loop `for` untuk memproses seluruh data | Dalam `hitung_kategori`, `simpang_baku`, dan `main` |
| Minimal satu function mengembalikan nilai | Semua function menggunakan `return` |
| Minimal satu proses numerik | Rata-rata dan simpang baku |
| Ringkasan: jumlah tiap kategori, rata-rata, maksimum, minimum | Dicetak di bagian `RINGKASAN` |
| Hasil wajib mencakup seluruh kategori | Dicek dengan `assert` di `main()` |
| 15 data inti dipertahankan, total tepat 20 | Dicek dengan `assert len(DATA_SNR) == 20` |

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
Jumlah RENDAH      : 6 data
Jumlah BAIK        : 8 data
Jumlah SANGAT BAIK : 6 data
Rata-rata SNR          : 15.25 dB
Simpang baku SNR       : 8.99 dB
Nilai maksimum         : 35 dB
Nilai minimum          : 0 dB
```

### Interpretasi Singkat

Dari 20 data, 6 data berada pada kategori RENDAH, 8 data pada kategori BAIK, dan 6 data pada kategori SANGAT BAIK. Rata-rata SNR sebesar 15,25 dB berada di kategori BAIK. Simpang baku sebesar 8,99 dB menunjukkan variasi nilai yang cukup besar, sehingga kondisi sinyal pada data ini tidak seragam.
