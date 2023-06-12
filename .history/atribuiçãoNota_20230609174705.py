def main():

    nota = int(input('Introduza a sua nota: '))

    avaliar_nota(nota)

#   print("A sua nota é", nota_avaliada)


def avaliar_nota(n):

    aux = ''

    if (n >= 0 and n < 10):
        aux = "NEGATIVA"
    elif (n >= 10 and n < 15):
        aux = "SUFICIENTE"
    elif n >= 15 and n < 18:
        aux = "BOM"
    elif n >= 18 and n <= 20:
        aux = "EXCELENTE"

    if n < 0 or n > 20:
        print('Valor inválido!!! Tem de inserir uma nota entre 0 e 20!!!')
    else:
        print('A sua nota é', aux)


main()
