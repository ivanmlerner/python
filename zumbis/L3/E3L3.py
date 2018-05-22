n = 0
while (1.03 ** n / 1.015 ** n) < 2.5:
    n += 1
print("Levará", n, "anos para a população de B alcançar A.")
