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
                print(vencedor(tentativa))
                break
            elif numero > porta:
                print('Para baixo')
            else:
                print('Mais para cima')

            tentativa += 1

            if tentativa > LIMITE:
                print(classifica(tentativa))
        except ValueError:
            print('ERROOOOOO')

def vencedor(tentativa):
    match tentativa:
        case 1:
            print('')
        case 2 | 3:
            print('')
        case 4 | 5:
            print('')
        case 6 | 7:
            print('')
        case 8 | 9:
            print('')    
        case 10:
            print('Vai à pesca... tiveste sorte')


main()
