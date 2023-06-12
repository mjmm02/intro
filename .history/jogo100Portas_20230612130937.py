import random

porta = random.randint(1, 100)

def main():

    tentativas = 0

    while True:
        num = int(print('Adivinhe o número da porta'))

        if num == rand:
            print('Ganhou o jogo!!')
            break
        elif num > rand:
                print('Mais baixo!')
        else:
             print('Mais alto!!')

        if tentativas == 5:
             print(Perdeu o jogo!!)
        i += 1    
        
    print()

main()