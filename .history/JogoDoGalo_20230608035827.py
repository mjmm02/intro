import random


print('-------------------------')
print('|     JOGO DO GALO      |')
print('-------------------------')
print()
print('        1|2|3    ')
print('        -----')
print('        4|5|6    ')
print('        -----')
print('        7|8|9    ')

player1 = {
      "name": 'human',
      'play': 0
}

player2 = {
      'name': 'cpu',
      'play': 0
}

board = ('1|2|3\n-----\n4|5|6\n-----\n7|8|9')

def jogada(player):

    aux = ""

    if player['name'] == 'human':
        board = board.replace(player[play], 'X')
    else:
        aux = 'O'
    board = board.replace(player[play], 'O')

    print(board)
        
        # aux = 1
        # for x in range(4):
        #     if x % 2 == 1:
        #         print('-----')
        #     else:
        #         for y in range(5):
        #             for w in range(aux, aux+2):
        #                 for z in p:
        #                     if y % 2 == 1:
        #                         print('|', end='')
        #                     else:
        #                         if p == z:
        #                             print('X', end='')
        #                         else:
        #                             print(' ', end='')
        #                 aux += 3

while True:

    cpu[play] = random.randint(1, 9)
    human[play] = int(input('Escolha a casa em que quer jogar: '))

    jogada(human)
    jogada(cpu)
