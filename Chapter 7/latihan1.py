try:
    nama_file = input("Masukkan nama file: ")
    print("Isi file dari", nama_file, "adalah: ")
    file = open(nama_file, 'r')
    print(file.read())

except FileNotFoundError:
    print('File tidak ditemukan')
