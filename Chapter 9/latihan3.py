def bintang1(n):
    for i in range(0, n//2):
        print(("*"*(2*i+1)).center(2*n-1))
        
def bintang2(n):
    for i in range(n//2, -2, -1):
        print(("*"*(2*i+1)).center(2*n-1))
        
def bintangFinal(n):
        bintang1(n)
        bintang2(n)

while True:
    baris=int(input('Masukkan jumlah baris : '))
    if (baris%2 == 1):
        bintangFinal(baris)
        break
    else:
        print('Bilangan harus ganjil')
        continue
        
