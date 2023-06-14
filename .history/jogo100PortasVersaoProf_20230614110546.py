def main():
    import random
    porta = random.randint(1, 100)
    print(porta)

    comecar_jogo()

# COMEÇAR O JOGO
def comecar_jogo(porta):

    LIMITE = 10
    tentativa = 1

    while True and tentativa < 10:
        try:
            numero = int(input(f'#{tentativa}: Qual é a casa de banho? '))

            if (numero == porta):
                print(f'yeayyyy acertaste à {tentativa}ª tentativa')
                break
            elif numero > porta:
                print('Para baixo')
            else:
                print('Mais para cima')

            tentativa += 1
        except:
            print('ERROOOOOO')


main()
