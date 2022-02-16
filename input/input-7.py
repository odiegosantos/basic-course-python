salario = int(input("Digite seu salário: "))
aumento = int(input("Digite a porcentagem de aumento: "))

aumento_porcento = ((salario * aumento) / 100)
novo_salario = (salario + aumento_porcento)

print(f"Novo salário R$: {novo_salario:5.2f}")