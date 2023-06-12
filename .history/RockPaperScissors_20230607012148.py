import random

choices = ['pedra', 'papel', 'tesoura']

rnd = random.randint(0, 2)

p = input('escolha pedra, papel ou tesoura: ')

c = choices[rnd]

print('Computador escolheu ' + c)
if p == 'pedra':
    if c == 'pedra':
        print('Empate!')
    elif c == 'papel':
        print('Perdeu!')
    else:
        print("Ganhou!")
elif p == 'papel':
    if c == 'pedra':
        print("Ganhou!")
    elif c == 'papel':
        print("Empate!")
    else:
        print('Perdeu!')
elif p == 'tesoura':
    if c == 'pedra':
        print('Perdeu!')
    elif c == 'papel':
        print('Ganhou!')
    else:
        print('Empate!')
else:
    print('Escolha inválida!')
