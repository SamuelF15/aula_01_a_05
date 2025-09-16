pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas_ordenadas_idades = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
print(pessoas_ordenadas_idades)