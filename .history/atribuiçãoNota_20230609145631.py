def main():

    nota = int(input('Introduza a sua nota: '))

    # avaliar_nota(nota)

    avaliar_nota(nota)

    # print("A sua nota é", nota_avaliação)

def nota_invalida(n):
    n = int(print('Introduza o valor da sua nota: '))
    avaliar_nota(n)

def avaliar_nota(n):

    aux = ''

    if n < 0 or n > 20:
        print("Valor inválido!")
        nota_invalida()

    elif (n < 10):
        aux = "NEGATIVA"
    elif (n >= 10 and n < 15):
        aux = "SUFICIENTE"
    elif n >= 15 and n < 18:
        aux = "BOM"
    elif n >= 18:
        aux = "EXCELENTE"

    print(aux)


main()
