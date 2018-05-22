usuario = input("Escolha um nome de usuário: ")

print(end = "E")
while input("scolha uma senha: ") == usuario:
    print("A senha não pode ser igual ao usuário, ", end = "e")

print("Senha válida.")
