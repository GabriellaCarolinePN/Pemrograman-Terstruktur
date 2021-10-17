# Input nilai
BhsIndonesia = int(input("Masukan nilai Bhs Indonesia = "))
IPA = int(input("Masukan nilai IPA = "))
Matematika = int(input("Masukan nilai Matematika = "))

# Syarat kelulusan
if (BhsIndonesia >= 60 and BhsIndonesia <= 100) and (IPA >= 60 and IPA <= 100) and (Matematika >= 70 and Matematika <= 100):
    print("Status Kelulusan : LULUS")
if (BhsIndonesia >= 0 and BhsIndonesia < 60) or (IPA >= 0 and IPA < 60) or (Matematika >= 0 and Matematika < 70):
    print("Status Kelulusan : TIDAK LULUS")
    print("Sebab")
    if (BhsIndonesia < 60):
        print("-Nilai Bahasa Indonesia kurang dari 60")
    if (IPA < 60):
        print("-Nilai IPA kurang dari 60")
    if (Matematika < 70):
        print("-Nilai Matematika kurang dari 70")
elif (BhsIndonesia < 0 or BhsIndonesia > 100) or (IPA < 0 or IPA > 100) or (Matematika < 0 or Matematika > 100):
    print("Maaf input ada yang tidak valid")
