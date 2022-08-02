"""
    Operadores Lógicos - Aula 4 - Usados para comparação.
    and, or, not
    in e not in
"""

# -----------------------------------------------------------------------------------------

# (Verdade 'E' Verdadeiro) =  Verdadeiro
# (Verdadeiro 'E' Falso) = False
comparacao1 and comparacao2

# -----------------------------------------------------------------------------------------

# (Verdadeiro 'OU' Verdadeiro)
comp1 or comp2

# -----------------------------------------------------------------------------------------

# Operador 'NOT' precisa só de uma expressao.
a = 2
b = 3

"""if not b > a: # Ele inverte uma expressao retornando false."""

# -----------------------------------------------------------------------------------------

# 'in' Operador pra saber se tem algo dentro da varíavel.

"""
nome = 'Johnny'

if 'J' in nome:
    print("Tem letra J no nome") 
"""

# -----------------------------------------------------------------------------------------

# Validação de senha e usário simples.
usuario = input('Nome do usuário: ')
senha = input('Senha: ')

usuario_bd = 'Johnny'
senha_bd = '123'

if usuario == usuario_bd and senha == senha_bd:
    print("Usuário e senha encontrado.")
else:
    print("Usuário e senha não encontrado.")
