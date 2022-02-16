dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

segundos_dia = dias * 86400   # segundos em 24 horas
segundos_horas = horas * 3600 # segundos em 1 hora
segundos_minutos = 60         # segundos em um minuto

soma_segundos = (segundos_dia + segundos_horas + segundos_minutos + segundos)

print(f"{soma_segundos} segundos no total")