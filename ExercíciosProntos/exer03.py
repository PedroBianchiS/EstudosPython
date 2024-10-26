def sumOrMult(a, b):
    if a == b:
        return a + b
    else:
        return a * b
    
a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))

c = sumOrMult(a, b)
print(c)