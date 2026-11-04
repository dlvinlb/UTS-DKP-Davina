"""
Pengujian fungsi kualitas_sinyal(snr) dari main.py dengan tampilan tabel.
Setiap input diambil dari DATA_SNR.
"""

from main import DATA_SNR, kualitas_sinyal

DATA_UJI = [
    (0, "RENDAH"),
    (3, "RENDAH"),
    (9, "RENDAH"),
    (10, "BAIK"),
    (11, "BAIK"),
    (18, "BAIK"),
    (19, "BAIK"),
    (22, "SANGAT BAIK"),
    (27, "SANGAT BAIK"),
    (35, "SANGAT BAIK"),
]


def tampilkan_pengujian():
    print("===== TEST kualitas_sinyal(snr) =====")
    print(f"| {'Input (dB)':<11}| {'Expected':<13}| {'Actual':<13}| Hasil |")
    for no, (snr, expected) in enumerate(DATA_UJI, start=1):
        assert snr in DATA_SNR, f"{snr} bukan data program"
        actual = kualitas_sinyal(snr)
        hasil = "PASS" if actual == expected else "FAIL"
        print(f"| {snr:<11}| {expected:<13}| {actual:<13}| {hasil} |")


if __name__ == "__main__":
    tampilkan_pengujian()
