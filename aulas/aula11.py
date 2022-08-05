"""
* Operadores Relacionais - Aula 4 - Usado para fazer compação.
* == > >= < <= !=
"""
# "=" Afirmando "==" Perguntando.
# Retorno Boolean.

#print(2 != 2)

nome = input("Qual seu nome?")
idade = input("Qual sua idade?")

# Limite para pegar empréstimo.

idade_menor = 20  # Muito jovem.
idade_maior = 30  # Passou da idade.

# Tera que convertem a idade para int porque input retorna str.
idade = int(idade)

if idade <= idade_menor:  # >= and idade_maior:
    print(f'{nome} não pode pegar o empréstimo pois está abaixo da idade miníma.')
elif idade > idade_maior:
    print(f'{nome} não pode pegar o empréstimo pois está acima da idade maxíma.')
else:  # Não terei outra checagem em else então só vai print.
    print(f'{nome} pode pegar o empréstimo')
