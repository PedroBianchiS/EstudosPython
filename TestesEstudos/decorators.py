def log_function(func):
    def wrapper(*args):
        print('Executando função...')
        return func(*args)
    return wrapper

def decoração(func):
    def interna(*args):
        print('Se liga na decoração!')
        return func(*args)
    return interna

@decoração
@log_function
def fala_mundo():
    return 'mundo'

@decoração
@log_function
def soma(x, y):
    return x + y

print(fala_mundo())
print(soma(2,3))