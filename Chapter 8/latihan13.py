def maksimal(a):
    tertinggi = 0 
    dictionary = {}
    for x in a:
        mid = x.get('mid')
        uas = x.get('uas')
        nilaiTertinggi = (mid + (2 * uas))/3
        if nilaiTertinggi > tertinggi:
            tertinggi = nilaiTertinggi
            dictionary['nim'] = x.get('nim')
            dictionary['nama'] = x.get('nama')
    print('Mahasiswa yang memiliki nilai akhir tertinggi ialah ' + dictionary['nama'] + ' dengan NIM ' + dictionary['nim'])

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

maksimal(nilaiMhs)
