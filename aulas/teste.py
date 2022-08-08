senha = input("Digite a senha: ")
tamanho_senha = len(senha)

while tamanho_senha < 8:
    print("Senha deve ter no minimo 8 dígitos.")
    break
else:
    print("Senha aceita.")
