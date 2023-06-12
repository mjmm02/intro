import random


def main():

    porta = random.randint(1, 100)
    print(porta)
    tentativas = 0
    resultado = ''

    while True:

        if tentativas <= 10:
            tentativas += 1

        

        print(str(tentativas) + 'ª tentativa!!')

        num = int(input('Adivinhe o número da porta entre 1 e 100: '))

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
        

        if tentativas < 10:
            if num > porta:
                print('Mais baixo!')
            else:
                print('Mais alto!!')

    print(resultado)


main()
