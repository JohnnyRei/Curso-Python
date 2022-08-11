"""
* Desempacotamento de listas em Python.
"""
lista = ["João", "Maria", "José", 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

# *outra_lista tem o restante dos valores. / ultimo_da_lista é o último valor.
n1, n2, *outra_lista, ultimo_da_lista = lista
# *_ quando você não se importa com resto dos valores.
print(n2)
