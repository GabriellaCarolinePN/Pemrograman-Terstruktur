sayur = ['bayam', 'kangkung', 'wortel', 'selada']

print('Daftar Sayur: ')
print(sayur)
print('Menu')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')

while True:
    pilihan = input('Pilihan Anda (A/B/C): ')
    if pilihan == 'A':
        tambah = input('Sayur apa yang ingin Anda tambahkan: ')
        sayur.append(tambah)
    elif pilihan == 'B':
        hapus = input('Sayur apa yang ingin Anda hapus dari daftar: ')
        if hapus in sayur:
            sayur.remove(hapus)
        else:
            print('Data tidak ditemukan')
    elif pilihan == 'C':
        print(sayur)
        lagi = input('Ingin melakukan pengolahan data lagi? (y/n)')
        if lagi == 'y':
            continue
        elif lagi == 'n':
            break
        else:
            print('Maaf input yang Anda masukkan salah')
            continue
    
        
        
        
        
        
        
