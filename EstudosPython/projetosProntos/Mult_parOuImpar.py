def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(mult(8, 10))

def parOuImpar(x):
    if x % 2 == 0:
        return 'Este número é par'
    return 'Este número é ímpar'

print(parOuImpar(4))
print(parOuImpar(7))