# Desafio aula 8 ano de nascimento.

nome = 'Johnny Guimarães'
idade = 22
altura = 1.74
e_maior = idade > 18
peso = 94
imc = peso/(altura ** 2)
ano_atual = 2022
ano_nascimento = ano_atual - idade

# Função format permite concatenar elementos em uma string por meio da formatação posicional.
print('{0} tem {1} de IMC e nasceu no ano {2}'.format(nome, imc, ano_nascimento))
