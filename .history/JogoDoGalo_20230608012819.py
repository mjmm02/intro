print('-------------------------')
print('|     JOGO DO GALO      |')
print('-------------------------')
print()
print('         | |     ')
print('        -----')
print('         | |     ')
print('        -----')
print('         | |     ')


player_pos = input('Escolha a casa em que quer jogar: ')

def jogada():
    for x in range(player_pos[0]):
        for y in range(player_pos[1]):
