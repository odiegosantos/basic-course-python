distancia = int(input("Qual é a distancia? "))
velocidade_media = int(input("Qual é a velocidade média "))

tempo_viagem = distancia / velocidade_media

# não retorna valor exato "falta calcular com maior precisão"
print(f"Tempo de viagem: {tempo_viagem:5.2f} horas")