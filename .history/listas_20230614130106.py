frutas = ['maçã', 'peras', 'bananas', 'morangos']

for i in range(len(frutas)):
    print(i, frutas[i])

i = len(frutas)

while i > 0:
    print(frutas[i])
    

frutas[3] = 'kiwi'

print(frutas)