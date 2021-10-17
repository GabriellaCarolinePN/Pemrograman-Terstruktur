import random

ScoreAnda = 100
AngkaRahasia = random.randint(0, 100)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0-100. Silakan tebak ya!!!')

while True:
    jawaban = int(input('\nTebakan Anda: '))

    if jawaban == AngkaRahasia:
        print('Yeeee... Bilangan tebakan Anda BENAR:-)')
        break #berhenti paksa
    elif jawaban != AngkaRahasia:
        ScoreAnda = ScoreAnda - 2
        print('Hehehe.. Bilangan tebakan Anda terlalu', 'kecil' if jawaban < AngkaRahasia
              else 'besar'
            )
    if ScoreAnda == 0:
        break
    
print('Score Anda : ', ScoreAnda)
