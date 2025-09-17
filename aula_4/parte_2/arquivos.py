import csv


caminho_do_arquivo = "C:/Users/samue/Cursos/Fazendo/Jornada_de_Dados/Bootcamp_Python_1_a_5/aula_4/parte_2/exemplo.csv"

arquivo_csv: list = []

with open(file=caminho_do_arquivo, mode="r", encoding='utf-8') as a:
    leitor_csv = csv.DictReader(a)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv) 

