#          Índices
#          0123456789...............................33
#          Precisa ser iterável = Precisa ter índices.
#          Iterar: passar sobre cada elemento da string.
#          += concatenação de strings.

frase = "O rato roeu a roupa do rei de roma"  # !Iterável
tamanho_da_frase = len(frase)
# print(frase[5])  # Ira printar a letra "o"
nova_string = ""
contador = 0

# while contador < tamanho_da_frase:  # colocou do tamanho da string.
#   print(frase[contador], contador)
#   contador += 1

# Transformando os 'r' em 'R' na nova string.

while contador < tamanho_da_frase:
    letra = frase[contador]
    if letra == "r":
        nova_string += "R"
    else:
        nova_string += letra
    contador += 1
print(nova_string)
