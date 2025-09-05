import numpy as np

matriz1 = np.random.randint(1, 11, size=(3, 3))
matriz2 = np.random.randint(1, 11, size=(3, 3))

soma = matriz1 + matriz2
multiplicacao = matriz1 * matriz2
transposta = soma.T

print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)
print("Soma:\n", soma)
print("Multiplicação elemento a elemento:\n", multiplicacao)
print("Transposta da soma:\n", transposta)
