frutas = ['maçã', 'peras', 'bananas', 'morangos']

for i in range(len(frutas)):
    print(i, frutas[i])

i = len(frutas)

while i > 0:
    i -= 1
    print(frutas[i])
    

frutas[3] = 'kiwi'

print(frutas)

def swap():
temp = frutas[arg1]
frutas[arg1] = frutas[arg2]
frutas[arg2] = temp 