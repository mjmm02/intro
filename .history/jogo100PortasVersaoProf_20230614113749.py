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
            while True:
                numero = int(input(f'#{tentativa}: Qual é a casa de banho? '))
                if numero in range(1, 100):
                    break
                else:
                    print('')

                if (numero == porta):
                    print(f'yeayyyy acertaste à {tentativa}ª tentativa')
                    print(classifica(tentativa))
                    break
                elif numero > porta and tentativa > LIMITE:
                    print('Para baixo')
                elif tentativa > LIMITE:
                    print('Mais para cima')

                tentativa += 1

                if tentativa > LIMITE:
                    print(classifica(tentativa))
        except ValueError:
            print('ERROOOOOO')


def classifica(tentativa):
    match tentativa:
        case 1:
            return 'És incrível!!!'
        case 2 | 3:
            return ('És quase incrível!!!')
        case 4 | 5:
            return ('Foste bonzinho... vá')
        case 6 | 7:
            return ('Quase no limite...')
        case 8 | 9:
            return ('Já se nota uma nódoa...')
        case 10:
            returnt('Vai à pesca... tiveste sorte')
        case _:
            return 'Vai trocar de ROUPA! \nA porta era a ' + porta


main()
