mahasiswa = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("=======================================================================")
print("NIM	  NAMA MAHASISWA          TANGGAL LAHIR        TEMPAT LAHIR")
print("-----------------------------------------------------------------------")

for data in mahasiswa:
    dataMhs = data.split(":")
    nim = (dataMhs[0]).ljust(9)
    nama = (dataMhs[1]).ljust(26)
    tglLahir = dataMhs[2]
    TglLahirLama = tglLahir.split("-")
    TglLahirBaru = ("/".join([TglLahirLama[2], TglLahirLama[1], TglLahirLama[0]])).ljust(17)
    tempatLahir = (dataMhs[3])
    print(nim, nama, TglLahirBaru, tempatLahir)

print("-----------------------------------------------------------------------")
