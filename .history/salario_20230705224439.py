def main():
    salario = 0
    nhoras = 0

    nhoras = int(input('Introduza o numero de horas trabalhadas: '))

    if nhoras >= 40:
        salario = (nhoras - 40) * 30 + 800
    else:
        salario = nhoras * 20
    
    print('O salário é', salario)

main()
