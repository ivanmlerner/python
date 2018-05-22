excesso = multa = 0
peso = float(input("Peso total de peixes (kg): "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

print("Excedeu o limite em " + str(excesso) + "kg\nMulta: R$" + str(multa))
