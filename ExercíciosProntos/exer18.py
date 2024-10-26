fran = 1.50
sara = 1.10

def saraMaiorFran(fran, sara):
    anos = 0
    while sara < fran:
        fran += 0.02
        sara += 0.03
        anos += 1

    return anos

print(f'Sara será maior que Franciso em {saraMaiorFran(fran, sara)} anos, quando ela terá {sara:.2f} e Francisco terá {fran:.2f}')