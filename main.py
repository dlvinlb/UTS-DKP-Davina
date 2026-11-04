"""
Monitoring Kualitas Sinyal / SNR
Kelompok B - Telekomunikasi
Nama : Davina Almira Alexandra
NIM  : 03041282631056
"""

import math

# 15 data inti
DATA_INTI = [5, 8, 11, 14, 18, 22, 27, 9, 16, 24, 12, 30, 7, 20, 15]

# 5 data tambahan
DATA_TAMBAHAN = [0, 3, 10, 19, 35]

# Gabungan 20 data yang akan diproses
DATA_SNR = DATA_INTI + DATA_TAMBAHAN


def kualitas_sinyal(snr):
    """Menentukan status kualitas sinyal dari nilai SNR (dB)."""
    if snr < 10:
        return "RENDAH"
    elif snr < 20:         
        return "BAIK"
    else:                  
        return "SANGAT BAIK"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori dan mengembalikannya sebagai dictionary."""
    jumlah = {"RENDAH": 0, "BAIK": 0, "SANGAT BAIK": 0}
    for snr in data:
        status = kualitas_sinyal(snr)
        jumlah[status] += 1
    return jumlah


def rata_rata(data):
    """Menghitung nilai rata-rata dari sekumpulan data."""
    return sum(data) / len(data)


def hitung_persentase(jumlah, total):
    """Menghitung persentase tiap kategori terhadap total data. Mengembalikan dictionary."""
    persen = {}
    for kategori, n in jumlah.items():
        persen[kategori] = n / total * 100
    return persen


def main():
    assert len(DATA_SNR) == 20, "Jumlah data harus tepat 20."

    print("=" * 52)
    print("MONITORING KUALITAS SINYAL / SNR")
    print("=" * 52)
    print(f"{'No':<4}{'SNR (dB)':>10}   {'Status':<12}{'Sumber'}")
    for no, snr in enumerate(DATA_SNR, start=1):
        sumber = "Inti" if no <= len(DATA_INTI) else "Tambahan"
        print(f"{no:<4}{snr:>10}   {kualitas_sinyal(snr):<12}{sumber}")

    jumlah = hitung_kategori(DATA_SNR)
    assert all(n > 0 for n in jumlah.values()), "Semua kategori harus terwakili."

    print("\n" + "=" * 52)
    print("RINGKASAN")
    print("=" * 52)
    persen = hitung_persentase(jumlah, len(DATA_SNR))
    for kategori, n in jumlah.items():
            print(f"Jumlah {kategori:<12}: {n} data ({persen[kategori]:.1f}%)")
    print(f"Rata-rata SNR          : {rata_rata(DATA_SNR):.2f} dB")
    print(f"Nilai maksimum         : {max(DATA_SNR)} dB")
    print(f"Nilai minimum          : {min(DATA_SNR)} dB")


if __name__ == "__main__":
    main()
