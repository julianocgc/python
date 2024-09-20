array = [
    {"nome": "Maria", "idade": 30},
    {"nome": "João", "idade": 25},
    {"nome": "Ana", "idade": 35}
]
array_ordenado = sorted(array, key=lambda x: x["nome"])
print(array_ordenado)  # Output: [{"nome": "Ana", "idade": 35}, {"nome": "João", "idade": 25}, {"nome": "Maria", "idade": 30}]