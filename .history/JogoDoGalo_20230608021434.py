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
    for x in range(1, 6):
        if x % 2 == 0:
            print('-----')
        else:
            aux = int(range(1,3))
            for y in (aux + x):
                for z in range((len(p)-1)):
                    if y % 2 == 1:
                        print('|', end='')
                    else:
                        if p == y:
                            print('X', end='')
                        else:
                            print(' ', end='')


player_pos.append(int(input('Escolha a casa em que quer jogar: ')))

jogada(player_pos)
