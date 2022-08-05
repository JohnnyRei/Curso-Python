"""
* Entrada de dados - Aula 03
"""

"""
# Atribuindo o valor de input na variável

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
# Print vazio para pular linha no output.
print()
print(
    f'O usuário digitou: {nome} tem {idade} e o tipo de variável é {type(nome)}')
"""

# Calculadora

# Tenho que fazer cast porque input por padrão e só str.

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_2 = int(numero_2)

print(numero_1 + numero_2)
