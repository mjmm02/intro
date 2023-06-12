import random



def main():

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
            tentativas += 1


main()
