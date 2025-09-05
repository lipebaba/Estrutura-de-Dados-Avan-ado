alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

soma = 0
for nota in alunos.values():
    soma += nota

media = soma / len(alunos)

print("Alunos e notas:", alunos)
print("Média da turma:", media)
