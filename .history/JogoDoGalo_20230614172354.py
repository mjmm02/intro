import os
import random

player1 = {
    "name": 'human',
    'num': 0
}

player2 = {
    'name': 'cpu',
    'num': 0
}

board = ('1|2|3\n-----\n4|5|6\n-----\n7|8|9\n')
board2 = (' | | \n-----\n | | \n-----\n | | \n')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def main():

    print('-------------------------')
    print('|     JOGO DO GALO      |')
    print('-------------------------')
    print()
    print('        1|2|3    ')
    print('        -----')
    print('        4|5|6    ')
    print('        -----')
    print('        7|8|9    ')

    while True:

        print(board2)
        move(player1)

        for i in board:
            if str(board[i]) != str(player1['num']) and board[i] == board[len(board)-1]):
                move(player1)
                i = 1
            elif board[i] == str(player1['num']):
                jogada(player1, i)
                break

        player2['num'] = random.randint(10)

        for j in board:
            while not board[j].isnumeric():
                player2['num'] = random.randint(10)

            jogada(player2, j)
            break


#       os.system('cls')


def move(p1):

    p1['num'] = int(input('Escolha a casa em que quer jogar: '))

    while p1['num'] > 9 or p1['num'] < 1:
        print('Escolha outro número!')
        p1['num'] = int(input('Escolha a casa em que quer jogar: '))


def jogada(p, pos):

    global board
    global board2
    aux = ''

    aux = list(board)

    if p['name'] == 'human':
        aux[pos] = 'X'
    else:
        aux[pos] = 'O'

    for i in aux:
        if aux[i].isnumeric():
            aux[i] = ' '

    board2 = "".join(aux)


main()
