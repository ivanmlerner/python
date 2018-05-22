um   = float(input("Lado 1: "))
dois = float(input("Lado 2: "))
tres = float(input("Lado 3: "))
if um + dois <= tres:
    print("Não formam um triângulo.")
elif um + tres <= dois:
    print("Não formam um triângulo.")
elif dois + tres <= um:
    print("Não formam um triângulo.")
elif um == dois and dois == tres:
    print("Formam umtriângulo equilátero.")
elif um == dois or dois == tres or um == tres:
    print("Formam um triângulo isóceles.")
else:
    print("Formam um triângulo escaleno.")
