"""
* while em Python - Aula 7
* utilizando para realizar ações enquanto
* uma condição for verdadeira.

* Requisitos: Entender condições e operadores.
"""

# Laços de repetição/ pense sempre como se foce um circulo.

"""
while True:  # Loop Infinito.
    nome = input("Qual seu nome? ")
    print(f"Olá, {nome}!")

print("Essa expressão não sera executada.")  # Fora do bloco while.
"""
# Quero exibir uma contagem até 100.

"""
x = 0

while x < 100:  # Quando x for menor que 100 laço passa a ser false.
    continue  # Sempre que achar essa palavra ele pula para proximo passo.
  # if x == 3:
  # x = x + 1
  # 'break' para o laço while

    print(x)
    x = x + 1

print("A contagem acabou!")
"""

while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite  outro númeroúmero: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? (S/N) ")

    if sair == "S":
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Digite apenas números!")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "/":
        print(num_1 / num_2)
    elif operador == "*":
        print(num_1 * num_2)
    else:
        print("Operador inválido!")
