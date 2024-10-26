string = 'Pedro'
método = 'método'

print(string)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())
else:
    print('NÃO EXISTE O MÉTODO', método)