# Input nilai
BhsIndonesia = int(input("Masukan nilai Bhs Indonesia = "))
IPA = int(input("Masukan nilai IPA = "))
Matematika = int(input("Masukan nilai Matematika = "))

# Syarat kelulusan
if (BhsIndonesia > 60) and (IPA > 60) and (Matematika > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")
