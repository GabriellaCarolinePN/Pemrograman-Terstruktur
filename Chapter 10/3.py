# program baca data mahasiswa
try:
    dataMhs = open("DataMhs.txt", "r")
    daftar = []
    isi = dataMhs.readlines()

    for i in range(len(isi)):
        pecah = isi[i].split("|")
        dictionary = {"NIM":pecah[0], "NAMA":pecah[1], "ALAMAT":pecah[2].replace("\n", "")}
        daftar.append(dictionary)
        
    print(daftar)

    dataMhs.close()
except FileNotFoundError:
    print("File tidak ditemukan")
