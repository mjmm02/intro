estudantes = []

with open('estudantes.csv') as file:
    for line in file:
        # row = line.rstrip().split(',')
        # print(row[0], "está na casa", row[1])

        nome, casa = line.rstrip().split(',')
        print(f'{nome} está na casa {casa}')
        estudante = {
            'nome': nome,
            'casa': casa 
        }
        # estudante['nome'] = nome
        # estudante['casa'] = casa
        estudantes.append(estudante)

# def get_nome(estudante):
#     return estudante['nome']        

# for estudante in sorted(estudantes, key=get_nome):
#     print(f"{estudante['nome']} está na casa {estudante['casa']}")

# def get_nome(estudante):
#     return estudante['nome']        

for estudante in sorted(estudantes, key=lambda estudante: estudante['nome']):
    print(f"{estudante['nome']} está na casa {estudante['casa']}")