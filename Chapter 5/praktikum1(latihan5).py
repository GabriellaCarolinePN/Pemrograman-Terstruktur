KodeKaryawan = input("Masukkan kode karyawan                       : ")
NamaKaryawan = input("Masukkan nama karyawan                       : ")
Golongan     = input("Masukkan golongan                            : ")

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

Status       = input("Masukkan status (Menikah/Belum Menikah)      : ")
if Status=="Menikah":
    JumlahAnak   = int(input("Masukkan jumlah anak                         : "))

if Status=="Menikah":
    TunjanganPasangan=(10/100)*GajiPokok
    TunjanganAnak=(5/100)*GajiPokok
    GajiKotor=GajiPokok+TunjanganPasangan+(TunjanganAnak*JumlahAnak)
else:
    GajiKotor=GajiPokok
GajiBersih=GajiKotor-((Potongan/100)*GajiPokok)

print("===========================================================")

print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")
print("Nama Karyawan     : ",NamaKaryawan, " ( Kode: ", KodeKaryawan, ")")
print("Golongan          : ", Golongan)
print("Status Menikah    : ", Status)
if Status=="Menikah":
    print("Jumlah Anak       : ", JumlahAnak)

print("-----------------------------------------------------------")
print("Gaji Kotor        : Rp", GajiKotor)
print("Potongan(", Potongan, "%)  : Rp", (Potongan/100)*GajiPokok)
print("--------------------------------------------------------- -")
print("Gaji Bersih       : Rp", GajiBersih)





















