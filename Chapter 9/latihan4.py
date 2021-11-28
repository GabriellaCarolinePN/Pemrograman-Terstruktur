import random

def randomString(teks, n):
    listKata = []
    i = 0
    while i < n:
        kata = "".join(random.sample(teks, len(teks)))
        if kata not in listKata:
            listKata.append(kata)
            i += 1
        else:
            continue
    return listKata

print(randomString(input("Masukkan kata: "), int(input("Masukkan angka: "))))

