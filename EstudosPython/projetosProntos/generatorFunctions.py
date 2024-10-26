def generator(n=0):
    yield 1 #pausa a execução da função
    print('carregando...')
    yield 2

gen = generator(n=0)
print(next(gen))
print(next(gen))