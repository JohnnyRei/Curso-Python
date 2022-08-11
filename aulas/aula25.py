"""
* Split, Join, Enumerate em Python

* Split - Divide uma string.
* Join - Junta uma lista.
! enumerate - numerar elementos de uma lista.
"""
#! .strip remove espaços no começo e no fim da string.

string = ("Eu sou o Homem de Ferro")
lista = string.split(" ")
# print(lista)  # ['Eu', 'sou', 'o', 'Homem', 'de', 'Ferro']

string2 = ",".join(lista)
print(string)
print(lista)
print(string2)

#! enumerate - numerar elementos de uma lista.

lista2 = [
    #   0       1         2
    ["João", "Paulo", "Pedro"],  # 0
    ["Laura", "Marcos", "Ana"],  # 1
    ["Caiu", "Maria", "Paula"]   # 2
]

# Posso dizer pra ele começar do valor diferenbte de 0. (lista2, 55):
for v1, v2 in enumerate(lista2):
    print(v1, v2)

#! () não posse adicionar nem remover elementos de uma tupla.
