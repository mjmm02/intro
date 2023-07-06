esytudantes = []

with open('estudantes.csv') as file:
    for line in file:
        # row = line.rstrip().split(',')
        # print(row[0], "está na casa", row[1])

        nome, casa = line.rstrip().split(',')
        print(f'{nome} está na casa {casa}')
