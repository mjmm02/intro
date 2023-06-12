def main():

    nota = int(input('Introduza a sua nota: '))

    # avaliar_nota(nota)

    nota_avaliação = avaliar_nota(nota)

    print("A sua nota é", nota_avaliação)

def nota_invalida()


def avaliar_nota(n):

    aux = ''

    if n < 0 or n > 20:
        print("Valor inválido!")
        main()

    elif (n < 10):
        aux = "NEGATIVA"
    elif (n >= 10 and n < 15):
        aux = "SUFICIENTE"
    elif n >= 15 and n < 18:
        aux = "BOM"
    elif n >= 18:
        aux = "EXCELENTE"

    return (aux)


main()
