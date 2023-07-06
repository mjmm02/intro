import time
import os


def main():

    digit = 0
    digit2 = 0
    digitm = 0

    while True:

        os.system('cls')
        analog(digitm)
        print('\n')
        analog(digit)
        print('\n')
        analog(digit2)
        #print('\n')
        time.sleep(1)
        #os.system('cls')
        digit2 += 1
        if digit2 > 9:
            digit += 1
            digit2 = 0
        if digit == :
            digit = 0
            digitm += 1
            


def analog(digit):

    if digit == 9:
        print('@@@\n@ @\n@@@\n  @\n  @\n@@@')
    elif digit == 8:
        print('@@@\n@ @\n@@@\n@ @\n@ @\n@@@')
    elif digit == 7:
        print('@@@\n  @\n  @\n @ \n @ \n @ ')
    elif digit == 6:
        print('@@@\n@  \n@@@\n@ @\n@ @\n@@@')
    elif digit == 5:
        print('@@@\n@  \n@@@\n  @\n  @\n@@@')
    elif digit == 4:
        print(' @@\n@ @\n@@ \n@@@\n @ \n @ ')
    elif digit == 3:
        print('@@@\n  @\n@@@\n  @\n  @\n@@@')
    elif digit == 2:
        print('@@@\n  @\n @ \n@  \n@  \n@@@')
    elif digit == 1:
        print(' @ \n@@ \n @ \n @ \n @ \n@@@')
    elif digit == 0:
        print('@@@\n@ @\n@ @\n@ @\n@ @\n@@@')


main()
