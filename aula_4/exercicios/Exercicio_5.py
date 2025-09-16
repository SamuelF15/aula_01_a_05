mercado = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
lista_de_compra = ["maçã", "banana", "cereja"]

vlr_lista = sum(mercado[item] for item in lista_de_compra)

print(vlr_lista)

# for i, j in enumerate(lista_de_compra):
#     for label, value in mercado.items():
#         # print(i,j,label,value)
#         if label == j:
#             vlr_lista += value
# print(vlr_lista)