valor = float(input('Digite o valor do produto: '))
print('Selecione a forma de pagamento: ')
formaPagamento = input('Dinheiro ou Pix=(D)\nA Vista no Crédito=(C)\nParcelado Três Vezes =(P)')

if formaPagamento == 'd':
    valor = valor - (15 * valor) / 100
    print(f'Valor a ser pago: {valor:.2f}')
elif formaPagamento == 'c':
    valor = valor - (10 * valor) / 100
    print(f'Valor a ser pago: {valor:.2f}')
elif formaPagamento == 'p':
    valor = valor + (10 * valor) / 100
    print(f'Valor a ser pago: {valor:.2f}')