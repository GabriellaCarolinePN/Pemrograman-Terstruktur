def luasSegitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas

alas = 10
tinggi = 20
print('Luas segitiga dg alas ', alas, ' dan tinggi ', tinggi, ' adalah ', luasSegitiga(alas, tinggi))

alas2 = 15
tinggi2 = 45
print('Luas segitiga dg alas ', alas2, ' dan tinggi ', tinggi2, ' adalah ', luasSegitiga(alas2, tinggi2))

total = (luasSegitiga(alas, tinggi) + luasSegitiga(alas2, tinggi2))
print("Total luas kedua segitiga tersebut adalah ", total)
