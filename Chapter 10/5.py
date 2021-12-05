# program membaca serangkaian data bilangan pada file
try:
    dataBil = open("SerangkaianBilangan.txt", "r")
    isi = dataBil.read()
    print("==Daftar Bilangan==")
    print(isi)
    dataBil.close()
except FileNotFoundError:
    print("File tidak ditemukan")

# jarak
print()

# program menghitung bilangan
try:
    dataBil = open("SerangkaianBilangan.txt", "r")
    daftar = []
    isi = dataBil.readlines()
    hasilJml = ''
    
    for data in range(len(isi)):
        pecah = isi[data].split("|")
        bil1 = pecah[0]
        bil2 = pecah[1]
        jml = int(pecah[0]) + int(pecah[1])
        hasilJml += str(jml) + '\n'

    dataBil.close()

    dataBil = open("HasilPenjumlahan.txt", "w")
    isi = dataBil.write(hasilJml)
    dataBil.close()

    print("==Hasil Penjumlahan==")
    dataBil = open("HasilPenjumlahan.txt", "r")
    print(dataBil.read())
    dataBil.close()

except FileNotFoundError:
    print()
    
