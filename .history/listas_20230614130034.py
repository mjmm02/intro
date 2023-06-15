frutas = ['maçã', 'peras', 'bananas', 'morangos']

for i in range(len(frutas)):
    print(i, frutas[i])

i = len(frutas)

while i > 0:
    print(frutas[i])
    i -= 1

frutas[3] = 'kiwi'

print(frutas)