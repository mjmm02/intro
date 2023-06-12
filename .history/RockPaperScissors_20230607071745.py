import random


while(True):
    choices = ['pedra', 'papel', 'tesoura']

    c = random.choice(choices)

    p = input('Escolha (pe)dra, (pa)pel ou (t)esoura: ')

    if p != 'pedra' and p != 'papel' and p != 'tesoura':
        print('Escolha inválida!')
        skip

    print('Computador escolheu ' + c)

    if c == p:
        print("Empate!")
    elif ((p == 'pedra' and c == 'tesoura') or (p == 'tesoura' and c == 'papel')
        or (p == 'papel' and c == 'pedra')):
        print('Ganhou!')
    else:
        print('Perdeu!')
    break