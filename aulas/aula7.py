# Uso de f strings.

nome = 'Johnny Guimarães'
idade = 22
altura = 1.74
e_maior = idade > 18
peso = 94
imc = peso/(altura ** 2)

# .2F para ter a saida de duas casas erradas.
print(f'{nome} tem {imc:.2F} de IMC')

# Função format permite concatenar elementos em uma string por meio da formatação posicional.
print('{0} tem {1} de IMC'.format(nome, imc))
