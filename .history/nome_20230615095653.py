import sys

# try:
#     print('Olá', sys.argv[1])
# except IndexError:
#     print('Poucos argumentos')

if len(sys.argv) < 2:
    sys.exit('Poucos argumentos')
elif len(sys.argv) > 2:
    print('Demasiados argumentos')

print('Olá', sys.argv[1])
