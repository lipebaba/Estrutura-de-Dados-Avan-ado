tempo_gasto = float(input("Qual foi o tempo gasto?"))
velocidade_media = float(input("Quka foi a velocidade media da viagem?"))

distancia = tempo_gasto * velocidade_media
print(distancia)

litros_usados = distancia/12
print(litros_usados)

print("velocidade_media:",velocidade_media)
print("Tempo gasto na viagem:", tempo_gasto)
print("Distancia percorrida:", distancia)
print("Quantidade de litros utilizados:", litros_usados)
