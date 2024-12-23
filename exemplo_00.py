CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bonus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o valor do bonus: "))

# 4) calcule o valor do bonus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus

print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

