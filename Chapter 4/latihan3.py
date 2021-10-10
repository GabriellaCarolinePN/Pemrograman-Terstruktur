import math

# Keterangan Soal
AMenujuC= 795
BBMPerLiter= 12
KapasitasLiterMobil= 50

# Menghitung Jumlah Liter Bensin yang diperlukan
LiterBensinYangDiperlukan= AMenujuC/BBMPerLiter

# Menghitung Berapa Kali Pengisian Bensin
KaliPengisianBensin= math.ceil(LiterBensinYangDiperlukan/KapasitasLiterMobil)

print("Minimal Pak Budi harus mengisi bensin sebanyak =", KaliPengisianBensin, "kali")
