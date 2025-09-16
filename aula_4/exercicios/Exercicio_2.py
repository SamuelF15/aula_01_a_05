lista = ["Python", "Java", "C++", "JavaScript",1]

for i, linguagem in enumerate(lista):
    if linguagem == "C++":
        lista.insert(i, "Ruby")
        lista.remove("C++")
    if linguagem == 1:
        break
print(lista)