string = ""
baris = 1

# Looping baris
while baris <= 5:
        kolom = baris

        # Looping kolom
        while kolom > 0:
                string = string + "* "
                kolom = kolom - 1

        string = string + "\n"
        baris = baris + 1
print(string)
