import random

def main():

    player1 = {
        "name": 'human',
        'num': 0
    }

    player2 = {
        'name': 'cpu',
        'num': 0
    }

    board = ('1|2|3\n-----\n4|5|6\n-----\n7|8|9\n')
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    print('-------------------------')
    print('|     JOGO DO GALO      |')
    print('-------------------------')
    print()
    print('        1|2|3    ')
    print('        -----')
    print('        4|5|6    ')
    print('        -----')
    print('        7|8|9    ')

    
def jogada(p):

    global board
    aux = ''

    for i in range(len(board)-1):
        if board[i] != 'X' and board[i] != 'O':
            if p['name'] == 'human':
                aux = 'X'
            else:
                aux = 'O'
            break

    board = board.replace(str(p['num']), aux)

    print(board)

main()