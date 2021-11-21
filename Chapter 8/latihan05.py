def kuadrat(bil):
    l=[]
    for i in range (len(bil)):
        bil[i] **= 2
    return bil

n = int(input('Jumlah bilangan yang ingin dimasukkan: '))
bil = []
i = 0
for i in range (n):
    input_bilangan = int(input('Masukkan bilangan: '))
    bil.append(input_bilangan)

print(kuadrat(bil))
