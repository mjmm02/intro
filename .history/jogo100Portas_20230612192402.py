import random


def main():

    porta = random.randint(1, 100)
    print(porta)
    tentativas = 0
    resultado = ''

    while True:

        if (tentativas <= 10):
             num = int(input('Adivinhe o número da porta entre 1 e 100: '))
             print(str(tentativas) + 'ª tentativa!!')
             
             while num < 1 or num > 100:
                    num = int(input('Tem de escolher um número entre 1 e 100!! '))
                    if num == porta:
                resultado = 'Acertou no número!! '
                if (tentativas < 3):
                    resultado += 'Boa pontaria!!'
                elif tentativas < 5:
                    resultado += 'Não precisava de vir a correr!!'
                elif tentativas < 8:
                    resultado += 'Ainda conseguia aguentar mais um pouco!!'
                elif tentativas <= 10:
                    resultado += 'Esteve perto dum acidente!!'
                break
            elif num > porta:
                print('Mais baixo!')
            else:
                print('Mais alto!!')
            tentativas += 1
        else:
            resultado = 'A casa de banho fica na porta Nº ' + \
                str(porta) + '!!\nErrou na porta e molhou-se nas calças, que embaraçoso!!'
            break

    print(resultado)


main()
