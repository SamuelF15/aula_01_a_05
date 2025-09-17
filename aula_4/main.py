# Era para fazer a tipagem usando "Type Hint" mas fiz na aula_3 sem querer kkkk  
fixo: int = 1000
print("-" * 25)
print("Vamos calcular seu Bônus!!!")
print("-" * 25)
try:
    # Loop para o nome
    while True:
        nome:str = input("*Qual o seu nome? ").strip()
        if not nome or any(char.isdigit() for char in nome):
            print("Campo obrigatório, não podendo conter números! Por favor, coloque seu nome.")
            continue
        break

    # Loop para o salário
    while True:
        try:
            salario:float = float(input("*Qual o seu salário? "))
            if salario < 0:
                print("O salário não pode ser menor que zero! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o salário.")

    # Loop para o bônus
    while True:
        try:
            bonus:float = float(input("*Qual o seu bônus? "))
            if bonus < 0:
                print("O bônus não pode ser menor que zero! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o bônus.")

    resultado_bonus = fixo + salario * bonus
    
    print(f"Parabéns {nome} tem um bônus de R$ {resultado_bonus:.2f}")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")

    