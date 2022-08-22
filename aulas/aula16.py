# Exercícios

""" 
* 1. Programa que pede um número inteiro a ser digitado e diz se ele e par ou ímpar.
* 2. Programa que pergunta a hora e da uma saudação dependendo do hórario informado. Ex: Bom dia 0-11,Boa Tarde 12-17 e Boa noite 18-23.
* 3. Programa que pede nome do usúario se tiver 4 letras ou menos retorna str "Seu nome é curto", 5 a 6 normal e maior que 6 retorna é muito grande.
"""
""" 
# 1.
num = input("Digite um número inteiro: ")

if num.isdigit():
    num = int(num)

    if num % 2 == 0:  # "==" Perguntando.
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")
else:
    print("Digite um número inteiro por favor")

"""

"""
# 2.
horas = input("Digite uma hora entre 0-23.: ")

if horas.isdigit():
    horas = int(horas)

    if horas < 0 or horas > 23:
        print("Erro digite um horario entra 0-23")
    elif horas <= 11:
        print("Bom dia!")
    elif horas >= 12 and horas <= 17:
        print("Boa Tarde!")
    elif horas >= 18 and horas <= 23:
        print("Boa Noite!")
else:
    print("Erro digite horas validas")
"""

# 3.
nome = input("Informe o nome do usuário: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Nome do usuário muito curto")
elif tamanho >= 5 and tamanho <= 6:
    print("Tamanho normal")
elif tamanho > 6:
    print("Nome usuário muito grande")
else:
    print("Não foi digitado um nome valido.")
