print('-------------------------')
print('|     JOGO DO GALO      |')
print('-------------------------')
print()
print('        1|2|3    ')
print('        -----')
print('        4|5|6    ')
print('        -----')
print('        7|8|9    ')

player_pos = []


def jogada(p):

    aux = 0

    board = (' | | \n-----\n | | \n-----\n | | ')


    for i in range(len(board)):
        if board[i] == ' ':
            if i == p:
                board.replace(board[i], 'X')

    
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


player_pos.append(int(input('Escolha a casa em que quer jogar: ')))

jogada(player_pos)