with open("nomes.txt", r) as file:
    lines = file.readlines()

for line in lines:
    print('Olá', line, sep)
f.read()