"""
Função 'len' para contar quantidade de caracteres.
"""

usuario = input("Digite o nome do usuário? ")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

# Quero saber se tem pelo menos 6 caracteres.

if qtd_caracteres < 6:
    print("Não digitou a quantidade mínima de caracteres que é 6.")
else:
    print("Você foi cadastrado no sistema")
