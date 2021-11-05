NamaFile = input('Masukkan Nama File : ')
file = open(NamaFile,'a')
ulangi = True
while(ulangi == True):
    data = input('Masukkan data yang akan ditambahkan: ')
    file.write(data)
    pilihan = input('Ingin menambahkan lagi?(y/n): ')
    if(pilihan == 'y'):
        ulangi = True
    elif(pilihan == 'n'):
        ulangi = False
    else:
        print('Input yang anda masukkan Tidak Valid')
        break
file.close()
