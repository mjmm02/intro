import os
import random

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
        
        
        move(player1)

        player2['num'] = numbers.pop(random.randint(1, 9))
        
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

        print(board)
        os.system('cls')

def move(p1):

    p1['num'] = int(input('Escolha a casa em que quer jogar: '))
    
    while p1['num'] > 9 and p1['num'] < 1:
            print('Escolha outro número!')
            p1['num'] = int(input('Escolha a casa em que quer jogar: '))
    


def jogada(p):

    global board
    global board2
    aux = ''

    for i in range(len(board)-1):
        if board[i] != 'X' and board[i] != 'O':
            if p['name'] == 'human':
                aux = 'X'
            else:
                aux = 'O'
            break

    board = board.replace(str(p['num']), aux)
    
    while j in board:
        if board[j] == aux:
            board2[i] = aux


main()