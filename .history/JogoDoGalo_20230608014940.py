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
player_pos.append(int(input('Escolha a casa em que quer jogar: ')))

def jogada(player_pos):
    for x in range(5):
        for y in range(5):
            for z in player_pos[y]:
                if y % 2 == 1:
                    print(' ')

                if player_pos == y:
                    print('X')
                else:
                    print(' ')




