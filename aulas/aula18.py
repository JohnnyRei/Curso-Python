"""
* Manipulando Strings - Aula 6

* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len abs, type, print, etc...
* Essas funções podem ser usadas diretamente em cada tipo.
"""

# Positivos [0123345678]
from this import d


texto = 'Python s2'

# Usando índice:

print(texto[2])  # Saída = t

# Negativos -[987654321]

url = 'http://www.google.com/'  # Quero remover a barra do final.

print(url[:-1])

nova_string = texto[2:6]  # Pegando só o 'thon' de python.

# Se eu quiser deis do começo coloco: [:6] / [0::] = pula de dois em dois.

print(texto[2])  # Saída = ts
