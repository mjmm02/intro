def main():
    maior = -1
    pede_numero(maior)
    print('O maior é:', maior)

def pede_numero(m):
    while True:
        num = int(input('Qual o número? '))
        if num < 0:
            break
        else:
            valida_maior(m, num)

def valida_maior(m):
    if num > m



main()