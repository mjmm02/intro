import sys

nomes = []

for _ in range(3):
    nomes.append(input("Nome? "))

# for nome in sorted(nomes):
#     print(f'Olá {nome}')

texto = ""
for nome in sorted(nomes):
    print