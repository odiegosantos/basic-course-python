n = 1
soma = 0
while n <= 2:
  x = int(input(f"Digite o {n} número: "))
  soma = soma + x
  n = n + 1
print(f"Média: {soma / 5:5.2f}")