livro_1 = {
    "Título": "Jornada de Dados",
    "Ano": 2004,
    "Autor": "Samuel",
    "Preço": 371.97
}

caracter = input("Digite um caracter para saber quantas vezes ele se repete:")

for label, value in livro_1.items():

    vlr_str = str(value)

    ocorrencias_label = label.upper().count(caracter.upper())
    ocorrencias_value = vlr_str.upper().count(caracter.upper())
    print(f"ocorrencias de '{caracter}' ou '{caracter.upper()}' em 'label' -> {label}: {ocorrencias_label}")
    print(f"ocorrencias de '{caracter}' ou '{caracter.upper()}' em 'value' -> {value}: {ocorrencias_value}")

        