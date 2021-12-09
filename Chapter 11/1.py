from datetime import *

def diffDate(x):
    HariIni = date.today()
    x = datetime.strptime(x, '%Y-%m-%d').date()
    selisih = HariIni - x
    return abs(selisih)

print(diffDate("2021-12-30").days)
