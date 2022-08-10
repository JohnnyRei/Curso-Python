"""
* Split, Join, Enumerate em Python

* Split - Divide uma string.
* Join - Junta uma lista.
* enumerate - Enumerar elementos de uma lista.
"""
#! .strip remove espaços no começo e no fim da string.

string = ("Eu sou o Homem de Ferro")
lista = string.split(" ")
# print(lista)  # ['Eu', 'sou', 'o', 'Homem', 'de', 'Ferro']

string2 = ",".join(lista)
print(string)
print(lista)
print(string2)

lista2 = [
    ["João", "Paulo", "Pedro"],  # 0
    ["Laura", "Marcos", "Ana"],  # 1
    ["Caiu", "Maria", "Paula"]   # 2
]
print(lista2[1][2])

#! () não posse adicionar nem remover elementos de uma tupla.
