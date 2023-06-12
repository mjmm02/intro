def main():
    maior = -1

    print('O maior é:', pede_numero(maior))


def pede_numero(m):
    while True:
        num = int(input('Qual o número? '))
        if num < 0:
            break
        else:
            valida_maior(m, num)
    


def valida_maior(m, num):
    if num > m:
        m = num
    return m


main()
