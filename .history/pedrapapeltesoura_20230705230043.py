import random

pw = 0
cw = 0


def main():

    str_vencedor = ''
    choices = ['pedra', 'papel', 'tesoura']

    pA = random.choice(choices)
    pB = random.choice(choices)

    print('Jogador A escolheu ' + pA)
    print('Jogador B escolheu ' + pB)

    if (pA == pB):
        str_vencedor = 'Empate!'
    elif ((pA == 'pedra' and pB == 'tesoura') or (pA == 'tesoura' and pB == 'papel')
            or (pA == 'papel' and pB == 'pedra')):
        str_vencedor = 'Jogador A venceu!'
    elif ((pB == 'pedra' and pA == 'tesoura') or (pB == 'tesoura' and pA == 'papel')
            or (pB == 'papel' and pA == 'pedra')):
        str_vencedor = 'Jogador B venceu!'

    print(str_vencedor)


main()
