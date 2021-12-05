# program mencari data mahasiswa berdasar nim
try:
    dataMhs = open("DataMhs.txt", "r")
    daftarNIM = []
    daftarNama = []
    daftarAlamat = []

    for data in dataMhs:
        pecah = data.split("|")
        daftarNIM.append(pecah[0])
        daftarNama.append(pecah[1])
        daftarAlamat.append(pecah[2])

    inputNIM = str(input('Masukkan NIM yang ingin dicari: '))
    print('================================================')
    if inputNIM in daftarNIM:
        call = daftarNIM.index(inputNIM)
        print('Data Mahasiswa: ')
        print('NIM    :', daftarNIM[call])
        print('Nama   :', daftarNama[call])
        print('Alamat :', daftarAlamat[call])
    else:
        print('Data Mahasiswa tidak ditemukan')

    dataMhs.close()
except FileNotFoundError:
    print('File tidak ditemukan')
