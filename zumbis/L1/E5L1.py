preco = float(input("Preço inicial: R$"))
des = float(input("Desconto em porcentagem: ")) / 100
preco_final = preco * (1 - des)
print("Preço descontado: R$", preco_final, "\nDesconto: R$", preco - preco_final)
