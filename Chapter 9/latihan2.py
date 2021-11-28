def bintang(n):
    for i in range(n):
        print(("*"*(2*i+1)).center(2*n-1))

n = int(input('Masukkan jumlah baris: '))
bintang(n)
