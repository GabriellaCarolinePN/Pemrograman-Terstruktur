n = int(input('Jumlah bilangan yang ingin dimasukkan: '))
list = []
i = 0
for i in range (n):
    input_bilangan = int(input('Masukkan bilangan: '))
    list.append(input_bilangan)
    list.sort(reverse = True)
print(list)
