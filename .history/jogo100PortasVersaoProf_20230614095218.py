def main():
    import random
    porta = random.randint(1, 100)
    print(porta)

    comecar_jogo()

# COMEÇAR O JOGO

def comecar_jogo(porta):

    LIMITE = 10
    tentativa = 1

    while True:
        numero = int(input('Qual é a casa de banho? '))

        if (numero == porta):
            print('yeayyyy')
            break
        elif numero > porta:
            print('Para baixo')
        else:
            print('Mais para cima')


main()
