import random


def main():

    porta = random.randint(1, 100)
    tentativas = 0
    resultado = ''

    while True:
        num = int(input('Adivinhe o número da porta entre 1 e 100: '))

        while num < 1 or num > 100:
            num = int(input('Tem de escolher um número entre 1 e 100!! '))

        if tentativas == 10:
            resultado = 'A casa de banho fica na porta número ' + \
                str(porta) + '!!\nerrou na porta e molhou-se!!'
            break
        elif num != porta:
            tentativas += 1
            print('Vai na', tentativas, 'ª tentativa!!')

        if num == porta:
            resultado = 'Ganhou o jogo!! '
            if (tentativas < 3):
                resultado += 'Muito bem!!'
            elif tentativas < 5:
                resultado += 'Ainda tem muito espaço na bexiga!!'
            elif tentativas < 8:
                resultado += 'Ainda conseguia aguentar mais um pouco!!'
            elif tentativas <= 10:
                resultado += 'Foi por pouco!!'
            break
        elif num > porta:
            print('Mais baixo!')
        else:
            print('Mais alto!!')

    print(resultado)


main()
