quilometros_percorridos = int(input("Quilometros percorridos: "))
quantidade_dias = int(input("Quantos dias com o carro: "))

valor_quilometro = quilometros_percorridos * 0.15
valor_dia = quantidade_dias * 60

total = valor_quilometro + valor_dia

print(f"Total a pagar: {total:5.2f}")