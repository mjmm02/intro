import os
import random

player1 = {
    "name": 'human',
    'num': ''
}

player2 = {
    'name': 'cpu',
    'num': ''
}

board = ('1|2|3\n-----\n4|5|6\n-----\n7|8|9\n')
board2 = (' | | \n-----\n | | \n-----\n | | \n')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
CLS = os.system('cls')


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

        print(board, '\n', board2)
        move(player1)

        for i in range(len(board) - 1):
            if board[i] != str(player1['num']) and board[i] == board[len(board)-1]:
                move(player1)
            elif board[i] == str(player1['num']):
                jogada(player1, i)
                break

        player2['num'] = random.randint(1, 9)

        for j in range(len(board) - 1):
            if board[j] == 'X' or board[j] == 'O' or board[j] == '|' or board[j] == '-' or board[j] == '\n':
                player2['num'] = str(random.randint(1, 9))
            else:
                jogada(player2, j)
                break


def move(p1):

    p1['num'] = str(int(input('Escolha a casa em que quer jogar: ')))

    # while p1['num'] > '9' or p1['num'] < 1:
    #     print('Escolha outro número!')
    #     p1['num'] = int(input('Escolha a casa em que quer jogar: '))


def jogada(p, pos):

    global board
    global board2
    aux = ''

    board2 = list(board2)
    board = list(board)

    if p['name'] == 'human':
        board[pos] = 'X'
        board2[pos] = 'X'
    else:
        board[pos] = 'O'
        board2[pos] = 'O'

    board = "".join(board)
    board2 = "".join(board2)


main()
