def main():
    
    nota = int(input('Introduza a sua nota: '))
    nota_avaliação = avaliar_nota(nota)
    
    if nota_avaliação < 0 and nota_avaliação > 20:
        print("Valor inválido!")
        avaliar_nota(nota)

    print("A sua nota é", nota_avaliação)

def avaliar_nota(n):

    aux = ''

    if (n < 0 and n > 20):
        aux = "Valor inválido!"
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
