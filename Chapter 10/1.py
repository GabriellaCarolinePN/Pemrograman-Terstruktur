# open dan print isi file
try:
    fileku = open("BilanganVertikal.txt", "r")
    isi = fileku.read()
    print(isi)
    fileku.close()
except FileNotFoundError:
    print("File tidak ditemukan")

# menghitung jumlah bilangan ganjil dan genap
try:
    fileku = open("BilanganVertikal.txt", "r")
    isi = fileku.read(1)
    ganjil = 0
    genap = 0

    for data in fileku:
        if (int(data)%2 == 1):
            ganjil += 1
        elif (int(data)%2 == 0):
            genap += 1

    print("Banyaknya bilangan genap:", genap)
    print("Banyaknya bilangan ganjil:", ganjil)
        
    fileku.close()
except FileNotFoundError:
    print()
