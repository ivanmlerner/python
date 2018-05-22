num = []

for n in range(int(input("Achar os extremos entre quantos números? "))):
    num.append(float(input("Digite o " + str(n + 1) + "º número: ")))

print("Maior:", max(num), "\nMenor:", min(num)) 
