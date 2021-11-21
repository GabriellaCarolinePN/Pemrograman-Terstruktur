buah = {'apel':5000, 'jeruk':8500, 'mangga':7800, 'duku':6500}
print('Daftar buah yang ada: ')
print(buah)
hargaBuah = []

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
