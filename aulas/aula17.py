"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2
# print(divisao)# 3.3333333333333335
# Se eu quiser mudar a saída poderia ser usado:
# print('{:.2f}'.format(divisao))  # '{:.2f}' duas casas decímais.
# ou
# print(f'{divisao:}')

nome = ("Johnny Guimarães")

print(f'{nome:*^50}')  # *****************Johnny Guimarães*****************

print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas
