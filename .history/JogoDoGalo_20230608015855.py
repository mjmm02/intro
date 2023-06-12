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
    for x in range(5):
        for y in range(1,10):
            for z in (len(player_pos)-1):
                if y % 2 == 1:
                    print('|', end=)
                else:
                    if p == y:
                        print('X')
                    else:
                        print(' ')

player_pos.append(int(input('Escolha a casa em que quer jogar: ')))

jogada(player_pos)