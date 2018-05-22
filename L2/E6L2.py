sal_tot = float(input("Quanto você ganha por hora? ")) * float(input("Quantas horas trabalhou no mês? "))
des = "Desconto para o"

print(des, "IR: R$" + str(0.11 * sal_tot))
print(des, "INSS: R$" + str(0.08 * sal_tot))
print(des, "sindicato: R$" + str(0.05 * sal_tot))
print("Salário líquido: R$" + str(0.24 * sal_tot))
