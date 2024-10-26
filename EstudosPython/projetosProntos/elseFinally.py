try:
    print('Abrir Arquivo')
    """ 8/0 """
except ZeroDivisionError:
    print('Erro! Dividiu por zero!')
else:
    print('Não Ocorreu Erro')
finally:
    print('Fechar Arquivo')