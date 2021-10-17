i = 1
hitung = 0
sum = 0

while i <= 100:
    print (i)
    hitung += 1
    i += 2
sum = int((hitung/2)*(2+((hitung-1)*2)))

print("Banyaknya bilangan ganjil: ", hitung)
print("Jumlah seluruh bilangan: ", sum)
