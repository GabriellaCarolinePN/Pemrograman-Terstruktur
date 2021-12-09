from datetime import *

# program input data peminjam buku
data_peminjam = open("DataPeminjamBuku.txt", "a")

while True:
    kode = input("Masukkan kode member: ")
    nama = input("Masukkan nama member: ")
    judul = input("Masukkan judul buku: ")
    tgl_pinjam = date.today()
    tgl_kembali = tgl_pinjam + timedelta(days=7)
    batas = kode + "|" + nama + "|" + judul + "|" + str(tgl_pinjam) + "|" + str(tgl_kembali) + "\n"

    data_peminjam.write(batas)

    pilihan = input("Ulangi input data (y/n): ")
    if pilihan == "y":
        continue
    elif pilihan == "n":
        break
    else:
        print("Input yang Anda masukkan salah")
data_peminjam.close()
    
# jarak
print()
print("==============DATA PEMINJAM BUKU==============")

# program baca file
file = open("DataPeminjamBuku.txt", "r")
isi = file.read()
print(isi)
file.close()
