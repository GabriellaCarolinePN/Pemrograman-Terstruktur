nilai = [{'nim' : 'A01', 'nama' : 'AGUSTINA', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'BUDI', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'CHICHA', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'DONNA', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'FATIMAH', 'mid' : 70, 'uas' : 100}]

print("===============================================")
print("NIM	NAMA		 N.MID	        N.UAS ")
print("-----------------------------------------------")

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(8), end='')
    print(nilai[i]['nama'].ljust(14), end='')
    print(str(nilai[i]['mid']).rjust(8), end='')
    print(str(nilai[i]['uas']).rjust(15))

print("-----------------------------------------------")
