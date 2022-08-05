"""
* While / Else - Aula 8 
* contadores 
* acumulados
"""
# O laço While precisa de um número.
# E possível usar else no laço while quando a expressão for falsa.

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print("chegou no else")
