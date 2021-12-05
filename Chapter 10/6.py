# program enkripsi file ke sandi caesar
teks = 'SAYA SUKA PYTHON'
listTeks = list(teks)
n = int(input('Masukkan banyak pergeseran yang dikehendaki: '))

# hasil enkripsi
sandi = ''
for huruf in listTeks:
    if huruf.isalpha():
      hurufAscii = ord(huruf)
      perpindahan = 65 + ((hurufAscii % 65) + n) % 26
      sandi += chr(perpindahan)
    else:
      sandi += ' '

print('Teks sandi:', sandi)
file = open('EnkripsiSandiCaesar.txt', 'w')
file.write(sandi)
file.close()
