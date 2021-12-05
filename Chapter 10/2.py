# program input data Mahasiswa
try:
    dataMhs = open("DataMhs.txt", "a")

    while True:
        nim = input("Masukkan NIM Anda: ")
        nama = input("Siapa Nama Anda: ")
        alamat = input("Dimana Alamat Anda: ")
        batas = nim + "|" + nama + "|" + alamat + "\n"

        dataMhs.write(batas)
        pilihan = input("Ulangi input data (y/n): ")
        if pilihan == "y":
            continue
        elif pilihan == "n":
            break
        else:
            print("Input yang Anda masukkan salah")

    dataMhs.close()
except FileNotFoundError:
    print("File tidak ditemukan")

# jarak
print("")

# program baca file
try:
    dataMhs = open("DataMhs.txt", "r")
    isi = dataMhs.read()
    print(isi)
    dataMhs.close()
except FileNotFoundError:
    print()
