fixo = 1000
print("-" * 25)
print("Vamos calcular seu Bônus!!!")
print("-" * 25)
nome = input("Qual o seu nome? ")
salario = float(input("Qual o seu salário? "))
bonus = float(input("Qual o seu bônus? "))

resultado_bonus = fixo + salario * bonus

print(f"Você {nome} te mum bônus de {resultado_bonus}")