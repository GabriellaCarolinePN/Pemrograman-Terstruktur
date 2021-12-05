# program deskripsi file dari sandi caesar
file = open("EnkripsiSandiCaesar.txt", "r")
isi = file.read()
listTeks = list(isi)
n = int(input('Masukkan banyak pergeseran yang dikehendaki: '))

# hasil deskripsi
asli = ''
for huruf in listTeks:
    if huruf.isalpha():
      hurufAscii = ord(huruf)
      perpindahan = 65 + ((hurufAscii % 65) - n) % 26
      asli += chr(perpindahan)
    else:
      asli += ' '

print('Teks asli:', asli)
file.close()

file = open('DeskripsiSandiCaesar.txt', 'w')
file.write(asli)
file.close()
