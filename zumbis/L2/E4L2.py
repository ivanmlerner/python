tot = int(input("Achar o maior entre quantos números? "))
num = []

for n in range(tot):
#    print("Digite o " + str(n + 1) + "º número:")
    num.append(float(input("Digite o " + str(n + 1) + "º número: ")))

maior = num[0]

for n in range(tot):
    if num[n] > maior:
        maior = num[n]

print("O maior número digitado foi", maior)
