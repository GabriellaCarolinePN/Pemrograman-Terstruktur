from random import randint
bil = 0, 1, 2, 3, 4, 6, 7, 8, 9, 10
hitung = 0

while True:
    bil = randint(0, 10)
    print(bil)
    hitung += 1
    if bil == 5:
        break
print(f'Jumlah Perulangan : {hitung}')
