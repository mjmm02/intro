def main():

    num = 0
    extenso = ''
    num = input('Introduza o seu numero: ')

    d = int(len(num)) -1 

    while d > 0:
        if (d == 3):
            if (num[d] == '1'):
                extenso += 'Mil' + extenso
            elif (num[d] == '2'):
                extenso += 'dois mil' + extenso
            elif (num[d] == '3'):
                extenso += 'Três mil' + extenso
            elif (num[d] == '4'):
                extenso += 'Quatro mil' + extenso
            elif (num[d] == '5'):
                extenso += 'Cinco mil' + extenso
            elif (num[d] == '6'):
                extenso += 'Seis mil' + extenso
            elif (num[d] == '7'):
                extenso += 'Sete mil' + extenso
            elif (num[d] == '8'):
                extenso += 'Oito mil' + extenso
            elif (num[d] == '9'):
                extenso += 'Nove mil' + extenso

        elif (d == 2):
            if (num[d] == '1'):
                extenso += 'Cento' + extenso
            elif (num[d] == '2'):
                extenso += 'Duzentos ' + extenso
            elif (num[d] == '3'):
                extenso += 'Trezentos ' + extenso
            elif (num[d] == '4'):
                extenso += 'Quatrocentos ' + extenso
            elif (num[d] == '5'):
                extenso += 'Quinhentos ' + extenso
            elif (num[d] == '6'):
                extenso += 'Seiscentos ' + extenso
            elif (num[d] == '7'):
                extenso += 'Setecentos ' + extenso
            elif (num[d] == '8'):
                extenso += 'Oitocentos ' + extenso
            elif (num[d] == '9'):
                extenso += 'Novecentos ' + extenso

        elif (d == 1):
            if (num[d] == '1'):
                extenso += 'Dez' + extenso
            elif (num[d] == '2'):
                extenso += 'Vinte ' + extenso
            elif (num[d] == '3'):
                extenso += 'Trinta ' + extenso
            elif (num[d] == '4'):
                extenso += 'Quarenta ' + extenso
            elif (num[d] == '5'):
                extenso += 'Cinquenta ' + extenso
            elif (num[d] == '6'):
                extenso += 'Sessenta ' + extenso
            elif (num[d] == '7'):
                extenso += 'Setenta ' + extenso
            elif (num[d] == '8'):
                extenso += 'Oitenta ' + extenso
            elif (num[d] == '9'):
                extenso += 'Noventa ' + extenso

        elif (d == 0):
            if (num[d] == '1'):
                extenso += 'Um' + extenso
            elif (num[d] == '2'):
                extenso += 'dois' + extenso
            elif (num[d] == '3'):
                extenso += 'Três' + extenso
            elif (num[d] == '4'):
                extenso += 'Quatro' + extenso
            elif (num[d] == '5'):
                extenso += 'Cinco' + extenso
            elif (num[d] == '6'):
                extenso += 'Seis' + extenso
            elif (num[d] == '7'):
                extenso += 'Sete' + extenso
            elif (num[d] == '8'):
                extenso += 'Oito' + extenso
            elif (num[d] == '9'):
                extenso += 'Nove' + extenso
        d -= 1

        print(extenso)


main()
