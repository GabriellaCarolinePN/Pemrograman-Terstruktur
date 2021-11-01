def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
    
def kombinasi(a, b):
    kombinasi = factorial(a) / (factorial(b) * factorial(a-b))
    print(kombinasi)

def permutasi(p, q):
    permutasi = factorial(p) / (factorial(p-q))
    print(permutasi)

kombinasi(5, 3)
permutasi(10, 7)
