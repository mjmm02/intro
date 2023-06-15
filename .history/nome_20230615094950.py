import sys

# try:
#     print('Olá', sys.argv[1])
# except IndexError:
#     print('Poucos argumentos')

if len(sys.argv) < 2:
    print('Poucos argumentos')
elif (len(sys.argv) > 2:
else:
    print('Olá', sys.argv[1])