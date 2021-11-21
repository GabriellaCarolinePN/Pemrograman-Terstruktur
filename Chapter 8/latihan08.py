def rerata(myData):
   myTuple = tuple(myData.values())
   jumlah = sum(myTuple)
   banyaknya = len(myTuple)
   RataRata = jumlah / banyaknya
   return RataRata
    
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Rata-rata dari keseluruhan buah adalah ' + str(rerata(buah)))
