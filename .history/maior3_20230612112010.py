
def main():

    num1, num2, num3 = int(input('Insira  o 1º número ')), int(
        input('Insira  o 2º número ')), int(input('Insira  o 3º número '))
    # num2 = int(input())
    # num3 = int(input())

    if (num1 > num2 and num1 > num3):
        maior = num1
    elif (num2 > num1 and num2 > num3):
        maior = num2
    elif num3 > num2 and num3 > num1:
        maior = num3
    else:
        maior = 'N/A'

    maior = num1
    if num2 > maior:
        maior = num2
        elif num

    print('O número maior é', maior)


main()
