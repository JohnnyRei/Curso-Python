"""
* Listas em Python
* Fatiamento
* append, insert, pop, del, clear, extend, min e max.
* range
"""

"""
# texto = ("valor") # Variável que recebe um valor SÓ.
# lista = [1, 2, 3, 4, 5, "Johnny", True, 10.5] # Lista recebe vários valores.

#         0    1    2    3    4
lista = ["A", "B", "C", "D", "E"]
# -       5    4    3    2    1

#lista[4] = "Qualquer outra coisa."

string = 'ABCDE'

print(lista[1])
"""
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1+l2  # ou l1.extend(l2)
l4 = list(range(0, 100, 8)) # 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88

for valor in l4: 
    print(valor)

l2.append("b")  # Adicionando valores a lista.
l1.insert(0, "a")  # Inceri um valor na lista.
l2.pop()  # Remove o último valor da lista.
del(l2[1:3])  # Remove os valores de 1 a 3.
print(max(l2))  # Retorna o maior valor da lista.
print(min(l2))  # Retorna o menor valor da lista.

print(l1)
print(l2)
"""
# Adivinhar o palavra.

secredo = "python"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print("Você perdeu.")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    digitadas.append(letra)
    if letra in secredo:
        print(f"A {letra} digitada existe na palavra.")
    else:
        print(f"A {letra} digitada não existe na palavra.")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secredo:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"
    if secreto_temporario == secredo:
        print("Você ganhou!!")
        break

    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")
    if letra not in secredo:
        chances -= 1  # chances = chances - 1
    print(f"Você ainda tem {chances} chances.")
