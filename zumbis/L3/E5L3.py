print("Máximo divisor comum.")

num1 = float(input("Informe um inteiro positivo: "))
while num1 < 0 or num1 % 1 != 0:
    num1 = float(input("Número inválido, informe um inteiro positivo: "))

num2 = float(input("Informe outro inteiro positivo: "))
while num2 < 0 or num2 % 1 != 0:
    num2 = float(input("Número inválido, informe outro inteiro positivo: "))

num1, num2 = int(num1), int(num2)

mdc = "MDC ="
if num1 == num2:
    print(mdc, num1)
elif num1 == 0:
    print(mdc, num2)
elif num2 == 0:
    print(mdc, num1)
else:
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    print(mdc, num1)
