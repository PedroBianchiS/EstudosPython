import sys

iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))   #basicamente um For :3
print(next(iterator))

""" lista = [n for n in range(1000)] """ #enquanto uma lista fica inteira contida na memória ocupando espaço
Generator = (n for n in range(1000)) #um generator dá apenas um valor por vezes, e seu tamanho não afeta seu peso em Bites

""" print(lista) """
print(Generator)

#medindo tamanhos em bites

""" print(sys.getsizeof(lista)) """
print(sys.getsizeof(Generator))

print(next(Generator))
print(next(Generator))
print(next(Generator))