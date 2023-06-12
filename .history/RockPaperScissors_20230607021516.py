import random

choices = ['pedra', 'papel', 'tesoura']

c = random.choice(choices)

p = input('Escolha (pe)dra, (pa)pel ou (t)esoura: ')

print('Computador escolheu ' + c)

if c == p:
    print("Empate!")
elif ((p == 'pedra' and c =)):

if p == 'pedra' or p == 'pe':
    if c == 'pedra':
        print('Empate!')
    elif c == 'papel':
        print('Perdeu!')
    else:
        print("Ganhou!")
elif p == 'papel' or p == 'pa':
    if c == 'pedra':
        print("Ganhou!")
    elif c == 'papel':
        print("Empate!")
    else:
        print('Perdeu!')
elif p == 'tesoura' or p == 't':
    if c == 'pedra':
        print('Perdeu!')
    elif c == 'papel':
        print('Ganhou!')
    else:
        print('Empate!')
else:
    print('Escolha inválida!')
