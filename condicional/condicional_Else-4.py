categoria = int(input("Qual categoria você utilizou este mês:"))
if categoria == 1:
    preco = 10
else: 
    if categoria == 2:
        preco = 20
    else:
      if categoria == 3:
          preco = 30
      else: 
        if categoria == 4:
            preco = 40
        else:
          if categoria == 5:
              preco = 50
          else:
            print("Categoria inválida, digite um valor entre 1 e 5")
            preco = 0
print(f"O preço do produto é: R${preco:6.2f}")