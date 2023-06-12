def main():

    nota = int(input('Introduza a sua nota: '))

    nota_avaliada = avaliar_nota(nota)

    print("A sua nota é", nota_avaliada)


def nota_invalida(n):

    

    return (n)


def avaliar_nota(n):

    aux = ''

    while n < 0 or n > 20:
        n = int(input('Valor inválido! Introduza novamente: '))

    if (n < 10):
        aux = "NEGATIVA"
    elif (n >= 10 and n < 15):
        aux = "SUFICIENTE"
    elif n >= 15 and n < 18:
        aux = "BOM"
    elif n >= 18:
        aux = "EXCELENTE"

    return (aux)


main()
