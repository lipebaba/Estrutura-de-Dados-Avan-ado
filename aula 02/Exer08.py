import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento

print("Matriz:\n", matriz)
print("Soma dos elementos:", soma)
