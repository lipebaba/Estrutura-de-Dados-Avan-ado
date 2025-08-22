M1 = float(input("Qual é a media 1?"))
M2 = float(input("Qual é a media 2?"))
M3 = float(input("Qual é a media 3?"))

M = (M1 + M2 + M3)/3

if M >= 0.0 and M <= 4.0:
    print("Reprovado")
elif M >= 4.1 and M <= 6.0:
    print("Pegou Exame")
    nota_exame = float(input("Nota do exame:"))
    if nota_exame >= 6.0:
        print("Aprovado")
elif M >= 6.0:
    print("Aprovado")

