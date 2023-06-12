import random

choices = ['pedra', 'papel', 'tesoura']

rnd = random.randint(1, 3)

p = input('escolha pedra, papel ou tesoura: ')

c = choices[rnd]

if p == 'pedra':
     if c == 'pedra':
          print('Empate!')
     elif c == 'papel':
          print('Perdeu!')
     else:
          print("Ganhou!")
elif p == 'papel':
    if c == 'pedra':
         print("Perdeu!")
    elif c == 'papel':
         print("Empate!")
    else:
         print()

    print('Perdeu!')
    else if p


switch()
