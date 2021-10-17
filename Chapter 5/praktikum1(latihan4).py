KodeKaryawan = input("Masukkan kode karyawan : ")
NamaKaryawan = input("Masukkan nama karyawan : ")
Golongan     = input("Masukkan golongan      : ")
if Golongan=="A":
    GajiPokok=10000000.00
    Potongan=2.5
if Golongan=="B":
    GajiPokok= 8500000.00
    Potongan=2.0
if Golongan=="C":
    GajiPokok=7000000.00
    Potongan=1.5
if Golongan=="D":
    GajiPokok=5500000.00
    Potongan=1.0
              
GajiBersih=GajiPokok-((Potongan/100)*GajiPokok)

print("===========================================================")

print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")
print("Nama Karyawan     : ",NamaKaryawan, " ( Kode: ", KodeKaryawan, ")")
print("Golongan          : ", Golongan)
print("-----------------------------------------------------------")
print("Gaji Pokok        : Rp", GajiPokok)
print("Potongan(", Potongan, "%)  : Rp", (Potongan/100)*GajiPokok)
print("--------------------------------------------------------- -")
print("Gaji Bersih       : Rp", GajiBersih)
