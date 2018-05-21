sal0 = float(input("Salário inicial: R$"))
aum = float(input("Aumento em porcentagem: ")) / 100
sal1 = sal0 + sal0 * aum
print("Novo salário: R$", sal1, "\nAumento: R$", sal1 - sal0)
