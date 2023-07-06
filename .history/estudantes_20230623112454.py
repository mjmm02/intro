with open('estudantes.csv') as file:
    for line in file:
        row = line.rstrip().split(';')
        print(row[0], "está na casa")