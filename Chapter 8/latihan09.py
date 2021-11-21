buah = {'apel':5000, 'jeruk':8500, 'mangga':7800, 'duku':6500}
print('Daftar buah yang ada: ')
print(buah)

pilihan = input('Nama buah yang dibeli: ')
if pilihan in buah.keys():
    kilo = int(input('Berapa Kg            : '))
    harga = kilo * buah[pilihan]
    print('--------------------------------')
    print('Total harga          : Rp' + str(harga) + ',-')
else:
    print('Maaf buah yang Anda masukkan tidak terdapat di dalam daftar')
