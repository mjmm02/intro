import random


def main():

    porta = random.randint(1, 100)
    tentativas = 0
    resultado = ''

    while True:
        num = int(input('Adivinhe o número da porta entre 1 e 100: '))

        while num < 1 or num > 100:
            num = int(input('Tem de escolher um número entre 1 e 100!! '))

        if tentativas == 0:
            resultado = 'A casa de banho fica no número da porta ' + \
            str(porta) + '!!\nPerdeu o jogo!!'
            break
        elif num != porta:
            print('Já fez', tentativas, 'tentativa/s!!')
            tentativas t = 1

        if num == porta:
            resultado = 'Ganhou o jogo!!'
            break
        elif num > porta:
            print('Mais baixo!')
        else:
            print('Mais alto!!')

    print(resultado)


main()
