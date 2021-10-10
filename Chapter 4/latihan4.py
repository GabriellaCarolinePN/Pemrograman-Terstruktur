import math

# Diketahui
JarakAB= 125
JarakBC= 256
KecepatanAB= 62
KecepatanBC= 70
JamBerangkat= 6
MenitBerangkat= 00

# Menghitung Jam Waktu Perjalanan
WaktuAB= round(JarakAB/KecepatanAB)
WaktuBC= round(JarakBC/KecepatanBC)

# Menghitung dari Berangkat sampai Istirahat
WaktuIstirahat= MenitBerangkat+45

# Menghitung Waktu Tiba
WaktutibadiC= JamBerangkat+WaktuAB+WaktuBC

print("Jadi Pak Amir sampai di Kota C pada pukul", WaktutibadiC,".",WaktuIstirahat)
