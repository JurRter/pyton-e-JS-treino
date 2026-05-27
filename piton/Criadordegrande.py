import random

nome = "teste_huffman.txt"
linhas = 10000
chars = 100

sequencias = [
    "A" * 20,
    "X" * 32,
    "B" * 10,
    "C" * 35,
    "D" * 45,
    "E" * 30,
    "M" * 18,
    "N" * 22,
    "P" * 28,
    "A" * 20,
    "R" * 15,
    "X" * 32,
    "T" * 12,
    "C" * 35,
    "D" * 45,
    "X" * 32,
    "Y" * 26,
    "X" * 32,
    "K" * 25,
    "Z" * 30,
    "S" * 8,
    "A" * 20,
    "C" * 35,
    "D" * 45,
    "G" * 60,
    "M" * 18,
    "N" * 22,
    "P" * 28,
    "A" * 20,
    "R" * 15,
    "X" * 32,
    "T" * 12,
    "C" * 35,
    "D" * 45,
    "X" * 32,
    "Y" * 26,
]

with open(nome, "w", encoding="utf-8") as arquivo:
    for _ in range(linhas):
        linha = ""

        while len(linha) < chars:
            linha += random.choice(sequencias)

        arquivo.write(linha[:chars] + "\n")

print(f"Arquivo '{nome}' gerado com sucesso!")
print(f"Linhas: {linhas}")
print(f"Caracteres por linha: {chars}")