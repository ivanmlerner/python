aux, fn = 1, 0
for n in range(int(input("Achar o enésimo número de fibonacci.\nN = "))):
    aux, fn = fn + aux, aux
print("F" + str(n+1), "=", fn)
