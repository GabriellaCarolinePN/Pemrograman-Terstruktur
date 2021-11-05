print('----------------------------------------')
print('--------PROGRAM HITUNG RATA-RATA--------')
print('----------------------------------------')

ulang = True
jumlah = 0
jumlah_bilangan = 0
while (ulang == True):    
    try:
        bil_bulat = int(input('Masukkan bilangan bulat: '))
        jumlah += bil_bulat
        jumlah_bilangan += 1
        pilihan = input('Lagi (y/n)? : ')
        if pilihan == 'y':
            ulang = True
        elif pilihan == 'n':
            ulang = False
        else:
            print('Input yang Anda masukkan salah')
            continue
    except ValueError:
        print('Harap masukkan bilangan bulat')
        continue
rata2 = jumlah / jumlah_bilangan
print('Rata-ratanya adalah ' + str(rata2))
