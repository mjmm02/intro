import random

pw = 0
cw = 0


def main():

    global pw
    global cw

    while True:
        choices = ['pedra', 'papel', 'tesoura']

        pA = random.choice(choices)

        pB = random.choice(choices)

        print('A escolheu ' + pA)
        print('B escolheu ' + pB)

        if (pA == pB):
            print("Empate!")
        elif ((pA == 'pedra' and pB == 'tesoura') or (pA == 'tesoura' and pB == 'papel')
              or (pA == 'papel' and c == 'pedra')):
            pw += 1
            if pw == 3:
                print('Ganhou!')
                break
        else:
            cw += 1
            if cw == 3:
                print('Perdeu!')
                break

        print('Jogador: ' + str(pw))
        print('Computador: ' + str(cw))


main()