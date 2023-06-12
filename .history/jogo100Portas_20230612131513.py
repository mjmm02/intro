import random


def main():

    porta = random.randint(1, 100)
    tentativas = 0

    while True:
        num = int(input('Adivinhe o número da porta: '))

        if num == porta:
            print('Ganhou o jogo!!')
            break
        elif num > porta:
            print('Mais baixo!')
        else:
            print('Mais alto!!')

        if tentativas == 5:
            print('Perdeu o jogo!!')
            break
        else:
            print('Restam ', tentativas, 'tentativas!')
            tentativas += 1


main()
