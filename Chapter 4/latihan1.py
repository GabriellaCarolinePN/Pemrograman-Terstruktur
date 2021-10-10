import math

# Diketahui
JamBerangkat= 6
MenitBerangkat= 0
JamTiba= 23
MenitTiba= 50
TarifSewa1= 200000
TarifSewa2= 10000

# Menghitung Waktu Sewa
JamSewaTambahan= JamTiba-JamBerangkat-12
MenitSewa= MenitTiba-MenitBerangkat

# Menghitung Tarif Sewa
TarifSewa= TarifSewa1+(JamSewaTambahan*TarifSewa2)+(round(MenitSewa*(TarifSewa2/60)))

print("Total tarif yang harus dibayarkan kepada rental adalah Rp", TarifSewa, ",-")
