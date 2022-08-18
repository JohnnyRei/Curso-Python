while True:
    contador = 10
    contador2 = 11
    cpfnum = ''
    accu2 = 0
    cpf = input('Digite seu CPF: (com pontos e traços) \n')
    for n in cpf:  # Itera sobre o cpf retirando pontos e traços
        if n == '.':
            continue
        elif n == '-':
            continue
    else:
        cpfnum = cpfnum + n  # Monta uma string com o CPF sem pontos ou traços
    for num in cpfnum:  # Itera sobre  o CPF realizando o calculo para gerar o digito 1
        accu1 = int(num) * contador
        accu2 = accu1+accu2
        contador -= 1
    if contador < 2:
        break
accu3 = 11 - (accu2 % 11)
# Utilização de operador ternário para verificar qual digito será
digito1 = 0 if accu3 > 9 else accu3
accu2 = 0
for num1 in cpfnum:  # Itera sobre o CPF realizando o calculo para gerar o digito 2
    accu1 = int(num1) * contador2
    accu2 = accu1 + accu2
    contador2 -= 1
    if contador2 < 2:
        break
accu4 = 11 - (accu2 % 11)
digito2 = 0 if accu4 > 9 else accu4
# Inverte a string do CPF para verificar os dois ultimo digitos
s1 = ''.join(reversed(cpfnum))
for rev in s1:  # Itera somente pelos dois primeiros digitos da string invertida verificando se condizem com a conta
    if int(rev) == digito2:
        continue
    elif int(rev) == digito1:
        print(
            f'O cpf digitado é: {cpf} e seus digitos são {digito1}, {digito2}, portanto o cpf é VALIDO')
        break
    else:
        print(f'O CPF digitado é invalido')
        break
