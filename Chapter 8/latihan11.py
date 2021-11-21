buah = {'apel':5000, 'jeruk':8500, 'mangga':7800, 'duku':6500}
print('Daftar Buah: ')
print(buah)
hargaBuah = []
print('Menu')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Keluar')

while True:
    pilihMenu = input('Pilihan Menu (A/B/C): ')
    if pilihMenu == 'A':
        tambahKeys = input('Masukkan nama buah: ')
        if tambahKeys in buah:
            print('Maaf nama buah sudah ada dalam daftar')
            continue
        tambahValues = int(input('Masukkan harga satuan: '))
        buah.update({tambahKeys:tambahValues})
        print(buah)
        continue
    elif pilihMenu == 'B':
        while True:
            pilihan = input('Nama buah yang dibeli: ')
            if pilihan in buah.keys():
                kilo = int(input('Berapa Kg            : '))
                harga = kilo * buah[pilihan]
                hargaBuah.append(harga)
                lagi =  input('Beli buah lagi? (y/n): ')
                if lagi == 'y':
                    continue
                elif lagi == 'n':
                    total = sum(hargaBuah)
                    print('--------------------------------')
                    print('Total harga          : Rp' + str(total) + ',-')
                    break
                else:
                    print('Maaf input yang Anda masukkan salah')
            else:
                print('Maaf buah yang Anda masukkan tidak terdapat di dalam daftar')
    elif pilihMenu == 'C':
        break
    else:
        print('Maaf input yang Anda masukkan salah')

