def starFormation1():
    string = ""
    baris = 1
    
    # Looping baris
    while baris <= 4:
            kolom = baris
    
            # Looping kolom
            while kolom > 0:
                    string = string + "* "
                    kolom = kolom - 1
    
            string = string + "\n"
            baris = baris + 1
    print((string), end='')

def starFormation2():
    string = ""
    baris = 3
    
    # Looping baris
    while baris >= 0:
        kolom = baris
    
        # Looping kolom
        while kolom > 0:
            string = string + "* "
            kolom = kolom - 1
    
        string = string + "\n"
        baris = baris - 1
    
    print(string)

starFormation1()
starFormation2()
