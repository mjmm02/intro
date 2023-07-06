estudantes = []

with open('estudantes.csv') as file:
    for line in file:
        # row = line.rstrip().split(',')
        # print(row[0], "está na casa", row[1])

        nome, casa = line.rstrip().split(',')
        print(f'{nome} está na casa {casa}')
        estudante = {
            'nome'
            casa: 
        }
        estudante['nome'] = nome
        estudante['casa'] = casa
        estudantes.append(estudante)

        for estudante in estudantes:
            print(f"{estudante['nome']} está na casa {estudante['casa']}")
