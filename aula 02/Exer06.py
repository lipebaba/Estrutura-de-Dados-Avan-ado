numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

soma = 0
for n in numeros:
    soma += n

print("Números digitados:", numeros)
print("Soma dos números:", soma)
