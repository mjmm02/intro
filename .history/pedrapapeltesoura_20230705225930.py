import random

pw = 0
cw = 0


def main():

    vencedor = ''
    choices = ['pedra', 'papel', 'tesoura']

    pA = random.choice(choices)
    pB = random.choice(choices)

    print('Jogador A escolheu ' + pA)
    print('Jogador B escolheu ' + pB)

    if (pA == pB):
        vencedor = 'Empate'
    elif ((pA == 'pedra' and pB == 'tesoura') or (pA == 'tesoura' and pB == 'papel')
            or (pA == 'papel' and pB == 'pedra')):
        vencedor = 'A venceu!'
    elif ((pB == 'pedra' and pA == 'tesoura') or (pB == 'tesoura' and pA == 'papel')
            or (pB == 'papel' and pA == 'pedra')):
        vencedor = 'B venceu!'

    print(vencedor + ' venceu!')


main()
