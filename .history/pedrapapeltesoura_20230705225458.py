import random

pw = 0
cw = 0


def main():

    
    choices = ['pedra', 'papel', 'tesoura']

    pA = random.choice(choices)
    pB = random.choice(choices)

    print('A escolheu ' + pA)
    print('B escolheu ' + pB)

    if (pA == pB):
        print("Empate!")
    elif ((pA == 'pedra' and pB == 'tesoura') or (pA == 'tesoura' and pB == 'papel')
            or (pA == 'papel' and pB == 'pedra')):
        print('Jogador A ganhou!')
    elif ((pB == 'pedra' and pA == 'tesoura') or (pB == 'tesoura' and pA == 'papel')
            or (pB == 'papel' and pA == 'pedra')):
        print('Perdeu!')

    print('Jogador ' + vencedor + ')


main()