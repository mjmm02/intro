def main():

    num = 0
    extenso = ''
    num = input('Introduza o seu numero: ')

    d = 0
    len_num = len(num) - 1

    while len_num >= 0:

        if (len_num == 3):
            if (num[d] == '0'):
                extenso += ''
            elif (num[d] == '1'):
                extenso += 'Mil '
            elif (num[d] == '2'):
                extenso += 'dois mil '
            elif (num[d] == '3'):
                extenso += 'Três mil '
            elif (num[d] == '4'):
                extenso += 'Quatro mil '
            elif (num[d] == '5'):
                extenso += 'Cinco mil '
            elif (num[d] == '6'):
                extenso += 'Seis mil '
            elif (num[d] == '7'):
                extenso += 'Sete mil '
            elif (num[d] == '8'):
                extenso += 'Oito mil '
            elif (num[d] == '9'):
                extenso += 'Nove mil '

            # if (num[d] != '0'):
            #     extenso += 'e '
            

        elif (len_num == 2):

            if (num[d - 1] != '0' or len_num  len(num) - 1):
                extenso += 'e '

            if (num[d] == '0'):
                extenso += ''
            elif (num[d] == '1'):
                if (num[d+1] == '0' and num[d+2] == '0'):
                    extenso += 'Cem '
                    break
                extenso += 'Cento '
            elif (num[d] == '2'):
                extenso += 'Duzentos '
            elif (num[d] == '3'):
                extenso += 'Trezentos '
            elif (num[d] == '4'):
                extenso += 'Quatrocentos '
            elif (num[d] == '5'):
                extenso += 'Quinhentos '
            elif (num[d] == '6'):
                extenso += 'Seiscentos '
            elif (num[d] == '7'):
                extenso += 'Setecentos '
            elif (num[d] == '8'):
                extenso += 'Oitocentos '
            elif (num[d] == '9'):
                extenso += 'Novecentos '

            # if (num[d] != '0'):
            #     extenso += 'e '

        elif (len_num == 1):

            if (num[d - 1] != '0'):
                extenso += 'e '

            if (num[d] == '0'):
                extenso += ''
            elif (num[d] == '1'):
                if (num[d+1] == '1'):
                    extenso += 'Onze'
                elif (num[d+1] == '2'):
                    extenso += 'Doze'
                elif (num[d+1] == '3'):
                    extenso += 'Treze'
                elif (num[d+1] == '4'):
                    extenso += 'Catorze'
                elif (num[d+1] == '5'):
                    extenso += 'Quinze'
                elif (num[d+1] == '6'):
                    extenso += 'Dezasseis'
                elif (num[d+1] == '7'):
                    extenso += 'Dezassete'
                elif (num[d+1] == '8'):
                    extenso += 'Dezoito'
                elif (num[d+1] == '9'):
                    extenso += 'Dezanove'
                elif (num[d+1] == '0'):
                    extenso += 'Dez'
                break
            elif (num[d] == '2'):
                extenso += 'Vinte '
            elif (num[d] == '3'):
                extenso += 'Trinta '
            elif (num[d] == '4'):
                extenso += 'Quarenta '
            elif (num[d] == '5'):
                extenso += 'Cinquenta '
            elif (num[d] == '6'):
                extenso += 'Sessenta '
            elif (num[d] == '7'):
                extenso += 'Setenta '
            elif (num[d] == '8'):
                extenso += 'Oitenta '
            elif (num[d] == '9'):
                extenso += 'Noventa '

            # if num[d] != '0':
            #     extenso += 'e '

        elif (len_num == 0):

            if (num[d - 1] != '0'):
                extenso += 'e '

            if (num[d] == '0'):
                if (num[d - 1] == '0' and num[d - 2] == '0' and num[d - 3] == '0'):
                    extenso += 'Zero'
                else:
                    extenso += ''
            if (num[d] == '1'):
                extenso += 'Um'
            elif (num[d] == '2'):
                extenso += 'Dois'
            elif (num[d] == '3'):
                extenso += 'Três'
            elif (num[d] == '4'):
                extenso += 'Quatro'
            elif (num[d] == '5'):
                extenso += 'Cinco'
            elif (num[d] == '6'):
                extenso += 'Seis'
            elif (num[d] == '7'):
                extenso += 'Sete'
            elif (num[d] == '8'):
                extenso += 'Oito'
            elif (num[d] == '9'):
                extenso += 'Nove'
        d += 1
        len_num -= 1

    print(extenso)


main()
