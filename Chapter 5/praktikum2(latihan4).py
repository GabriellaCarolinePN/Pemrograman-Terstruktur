string = ""
baris = 5

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
