area = float(input("Qual a área a ser pintada? "))

num_latas = int(area // 54) + int(bool(area % 54))

print("Serão necessárias", num_latas, "de tinta.\nPreço total: R$" + str(80 * num_latas) + ".00")
