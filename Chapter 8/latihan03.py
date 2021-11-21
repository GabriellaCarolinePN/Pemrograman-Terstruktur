n = int(input('Jumlah nama yang ingin dimasukkan: '))
list_nama = []
i = 0
for i in range (n):
    nama_mahasiswa = input('Masukkan nama mahasiswa: ')
    list_nama.append(nama_mahasiswa)
    list_nama.sort()
print(list_nama)

x = 0
for x in range (len(list_nama)):
    print(list_nama[x] + ' (', len(list_nama[x]), 'karakter )')
    x += 1
