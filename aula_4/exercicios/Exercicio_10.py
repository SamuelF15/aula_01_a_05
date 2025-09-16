valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = [pares for pares in valores if pares % 2 == 0] 
lista_impares = [impares for impares in valores if impares % 2 != 0]

print(f"Pares: {lista_pares}\n"
      f"Impares: {lista_impares}")
