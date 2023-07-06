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

        os.system('cls')
        print(board, '\n', board2)
        move(player1)

        jogada(player1)

        # for i in range(1, 9):
        #     if board[i] == board[len(board)-1]:
        #         move(player1)
        #     elif i == player1['num']:
        #         jogada(player1, i)
        #         break
        #     i = 0

        player2['num'] = random.randint(1, 9)

        for j in range(len(board) - 1):
            if board[j] == 'X' or board[j] == 'O' or board[j] == '|' or board[j] == '-' or board[j] == '\n':
                player2['num'] = str(random.randint(1, 9))
                j = 0
            else:
                jogada(player2, j)
                break

        end_condition = board2.find(' ')
        if end_condition == -1:
            print(board2, '\n')
            print('GAME OVER YEAAAAAAAAAAAAAAHHHHHHHHHH')
            break


def move(p1):

    aux = 0

    while aux > 9 or aux < 1:
        aux = int(input('Escolha a casa em que quer jogar (1 - 9): '))
    
    p1['num'] = aux


def jogada(p):

    global board
    global board2
    aux = ''

    board2 = list(board2)
    board = list(board)

    if p['name'] == 'human':
        numbers[p[]] = 'X'
        board2[pos] = 'X'
    else:
        board[pos] = 'O'
        board2[pos] = 'O'

    board = "".join(board)
    board2 = "".join(board2)


def win_condition():

    if (pos[0] == pos[1] and pos[0] == pos[2] and pos[1] == pos[2]):
        if pos[0] == player1['token']:
            print('Ganhou o jogo!!!')
        else:
            print('Perdeu o jogo!!')

main()
