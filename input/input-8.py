mercadoria = int(input("Valor da mercadoria: "))
desconto = int(input("Porcentagem de desconto: "))

desconto_porcento = ((mercadoria * desconto) / 100)
novo_valor = (mercadoria - desconto_porcento)

print(f"Valor com desconto R$: {novo_valor:5.2f}")