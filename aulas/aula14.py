"""
* Checando o que foi digitado antes de fazer a conta.
"""

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print("Não foi possível converter os números para realizar a conta.")
