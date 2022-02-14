categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
  preco = 10
elif categoria == 2:
  preco = 20
elif categoria == 3:
  preco = 30
elif categoria == 4:
  preco = 40
elif categoria == 5: 
  preco = 50
else :
  print("Categoria inválida, digite um valor entre 1 e 5")
  preco = 0
print(f"O preço do produto é: R${preco:6.2f}")