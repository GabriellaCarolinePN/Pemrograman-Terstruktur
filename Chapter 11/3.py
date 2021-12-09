from datetime import *

def diffDate(x):
    tglPengembalian = datetime.date(datetime.now())
    x = datetime.strptime(x, "%Y-%m-%d").date()
    return int((tglPengembalian - x).days)

inputKode = input("Masukan kode member yang ingin dicari : ")

file = open("DataPeminjamBuku.txt","r")

hasil = False
for data in file:
    data_copy = data.split("|").copy()
    kode = data.split("|")[0]
    if(kode == inputKode):
        hasil = data_copy
        break
        
if hasil:
    TglMaksPinjam = hasil[4].rstrip('\n')
    terlambat = diffDate(TglMaksPinjam)
    if(terlambat <= 0):
        Kal_Terlambat = "Tidak Terlambat"
        denda         = "Tidak Ada Denda"
    elif(terlambat > 0):
        Kal_Terlambat = str(terlambat) + " hari"
        denda         = "Rp " + str(terlambat*2000)

    print("=================================================")
    print("Data Peminjaman Buku")
    print("Kode Member                 :", hasil[0])
    print("Nama Member                 :", hasil[1])
    print("Judul Buku                  :", hasil[2])
    print("Tanggal Mulai Peminjaman    :", hasil[3])
    print("Tanggal Maks Peminjaman     :", TglMaksPinjam)
    print("Tanggal Pengembalian        :", datetime.date(datetime.now()))
    print("Terlambat                   :", Kal_Terlambat)
    print("Denda                       :", denda)
else:
    print("Data peminjam tidak ditemukan")
