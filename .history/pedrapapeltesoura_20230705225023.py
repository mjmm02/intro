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

        if (c == p):
            print("Empate!")
        elif ((p == 'pedra' and c == 'tesoura') or (p == 'tesoura' and c == 'papel')
              or (p == 'papel' and c == 'pedra')):
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