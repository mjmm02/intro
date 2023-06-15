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

        

        for i in range(len(board) - 1):
            while not board[i] == str(player1['num']):
                move(player1)
                break
            elif board[i]:
                print('Escolha outro número!')
                continue

        player2['num'] = random.randint(10)

        for j in range(len(board) - 1):
            while not board[j].isnumeric():
                player2['num'] = random.randint(10)
                
            jogada(player2)
            break


#       os.system('cls')


def move(p1):

    p1['num'] = int(input('Escolha a casa em que quer jogar: '))

    while p1['num'] > 9 and p1['num'] < 1:
        print('Escolha outro número!')
        p1['num'] = int(input('Escolha a casa em que quer jogar: '))


def jogada(p):

    global board
    global board2
    aux = ''

    for i in range(len(board) - 1):
        if board[i] != 'X' and board[i] != 'O':
            if p['name'] == 'human':
                aux = 'X'
            else:
                aux = 'O'
            break

    board = board.replace(str(p['num']), aux)

    # for j in range(len(board)-1):
    #     if board[j].isnumeric() and board[j] != 'O' and board[j] != 'X':
    #         board = board.replace(str(j), ' ', 1)


main()
