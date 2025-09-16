fixo = 1000
print("-" * 25)
print("Vamos calcular seu Bônus!!!")
print("-" * 25)

# Loop para o nome
while True:
    nome = input("*Qual o seu nome? ").strip()
    if not nome.strip():
        print("Campo obrigatório! Por favor, coloque seu nome.")
        continue
    break

# Loop para o salário
while True:
    try:
        salario = float(input("*Qual o seu salário? "))
        if salario < 0:
            print("O salário não pode ser menor que zero! Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o salário.")

# Loop para o bônus
while True:
    try:
        bonus = float(input("*Qual o seu bônus? "))
        if bonus < 0:
            print("O bônus não pode ser menor que zero! Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o bônus.")

resultado_bonus = fixo + salario * bonus

print(f"Parabéns {nome} tem um bônus de R$ {resultado_bonus:.2f}")