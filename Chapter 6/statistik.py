def sum(*myData):
    sum = 0
    i = 0

    for data in myData:
        sum += data

    jumlah = sum 
    print(jumlah)

def average(*myData):
    sum = 0
    i = 0

    for data in myData:
        sum += data
        i += 1

    rata2 = sum / i
    print('Rata-ratanya : ', rata2)

def maksimal(*myData):
    i = myData
    print('Nilai Maksimal : ', max(i))

def minimal(*myData):
    i = myData
    print('Nilai Minimal : ', min(i))
    
