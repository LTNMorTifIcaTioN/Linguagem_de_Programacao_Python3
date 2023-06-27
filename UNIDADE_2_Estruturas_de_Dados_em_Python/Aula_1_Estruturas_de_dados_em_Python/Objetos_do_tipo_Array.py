"""
A biblioteca NumPy, criada especificamente para a computação científica com Python. O NumPy contém, entre outras coisas:

um poderoso objeto de matriz (array) N-dimensional.
funções sofisticadas.
ferramentas para integrar código C/C++ e Fortran.
recursos úteis de álgebra linear, transformação de Fourier e números aleatórios.

Para utilizar a biblioteca NumPy é preciso fazer a instalação com o comando 'pip install numpy'.
É necessário importar a biblioteca para o projeto, como o comando import numpy.
"""

print('In[23]')

import numpy

matriz_1_1 = numpy.array([1, 2, 3])  # Cria matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1, 2], [3, 4]])  # Cria matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]])  # Cria matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]])  # Cria matriz 2 linhas e 3 colunas

print(type(matriz_1_1))
print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)

print()
print('==============================================================================================================')


# Construções de matrizes usadas em álgebra linear já prontas, com um único comando:

print('In[24]')

m1 = numpy.zeros((3, 3))  # Cria matriz 3 x 3 somente com zero
m2 = numpy.ones((2, 2))  # Cria matriz 2 x 2 somente com um
m3 = numpy.eye(4)  # Cria matriz 4 x 4 identidade
m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5)  # Cria matriz 2 X 5 com números inteiros

print('\n numpy.zeros((3, 3)) = \n', numpy.zeros((3, 3)))
print('\n numpy.ones((2,2)) = \n', numpy.ones((2, 2)))
print('\n numpy.eye(4) = \n', numpy.eye(4))
print('\n m4 = \n', m4)

print(f"Soma dos valores em m4 = {m4.sum()}")
print(f"Valor mínimo em m4 = {m4.min()}")
print(f"Valor máximo em m4 = {m4.max()}")
print(f"Média dos valores em m4 = {m4.mean()}")