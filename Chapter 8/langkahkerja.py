# Membuat list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3, 10)
b.insert(2, 15)
a.append(4)
b.append(8)
a.sort()
b.sort()
print('a = ', end='')
print(a)
print('b = ', end='')
print(b)

# Membuat list c dan d
c = a[0:8]
d = b[2:10]
print('c = ', end='')
print(c)
print('d = ', end='')
print(d)

# Membuat list e
e = []
i = 0
for i in range(len(c) and len(d)):
    r = c[i] + d[i]
    e += [r]
print('e = ', end='')
print (e)

# Mengubah list e ke tuple
myList = e
myTuple = tuple(myList)
print('myTuple = ', end='')
print(myTuple)

# Mencari nilai minimal, maksimal, dan jumlah seluruh elemen e
print('Nilai minimal dari elemen e = ', end='')
print(min(myTuple))
print('Nilai maksimal dari elemen e = ', end='')
print(max(myTuple))
print('Jumlah seluruh elemen e = ', end='')
print(sum(myTuple))

# Membuat string myString
myString = 'python adalah bahasa pemrograman yang menyenangkan'
mySet = set(myString)
print('Huruf penyusun dari \'python adalah bahasa pemrograman yang menyenangkan\' = ', end='')
print(mySet)

# Mengubah set ke list
myList2 = list(mySet)
myList2.sort()
print('Huruf penyusun dari \'python adalah bahasa pemrograman yang menyenangkan\' secara urut = ', end='')
print(myList2)








