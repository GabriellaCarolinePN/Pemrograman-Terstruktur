def dataStat(x):
    list_value = []
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    list_value.extend([a, b, c])
    return(a, b, c)

n = int(input('Jumlah bilangan yang ingin dimasukkan: '))
list = []
i = 0
for i in range (n):
    input_bilangan = int(input('Masukkan bilangan: '))
    list.append(input_bilangan)
    list.sort(reverse = True)
print(dataStat(list))
