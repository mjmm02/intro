
def main():

    while True:
        print('1 - Acrescentar nomes')
        print('2 - Ler nomes da lista')
        print('3 - Ordenar lista')
        print('9 - Sair')
        escolha = int(input())

        if escolha == 1:
            acrescentar_nomes()
        elif escolha == 2:
            ler_nomes()
        elif escolha == 3:
            ordenar_nomes()
        elif escolha == 9:
            break
        else:
            print('\nEscolha inválida!!\n')


def acrescentar_nomes():
    f = open('nomes.txt', 'a')
    nome = input('Introduza um nome para a lista: ')
    f.write(nome)
    f.close()


def ler_nomes():
    f = open('nomes.txt', 'r')
    print(f.read())
    f.close()


def ordenar_nomes():

    list = []
    
    with open('nomes.txt', 'r') as f
        for line in f:


    list = f.read()

    list.sort()
    f.close()
    
    f = open('nomes.txt','w')
    f.write(list)
    f.close()

main()
