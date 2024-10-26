import numpy as np
from random import randint

i = int(input('Digite a altura da matriz: '))
j = int(input('Digite a largura da matriz: '))

matrizAleatória = np.random.randint(0,10, size=(i, j))

print(matrizAleatória)