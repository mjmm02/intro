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

        player2['num'] = numbers.pop(random.randint(0, len(numbers) - 1))

        for i in range(len(board) - 1):
            if board[i] == str(player1['num']):
                jogada(player1)
                break
            if i == (len(board) - 2):
                print('Escolha outro número!')
                continue

        for j in range(len(board) - 1):
            if (board[j] == str(player2['num'])) and (player1['num'] != player2['num']):
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

    for j in range(len(board) - 1):
        if board[j] == aux:
            board2[j] = board[j]

main()
