import time

def main():

    digit = 9

    while True:

        analog(digit)
        time.sleep(1)
        digit 




def analog(digit):

    if digit == 9:
        print(' @ \n@ @\n @ \n  @\n  @\n @@')
    elif digit == 8:
        print(' @ \n@ @\n @ \n@ @\n@ @\n @ ')
    elif digit == 7:
        print('@@@\n  @\n  @\n @ \n @ \n@  ')
    elif digit == 6:
        print('@@@\n@  \n @ \n@ @\n@ @\n @ ')
    elif digit == 5:
        print('@@@\n@  \n@@@\n@ @\n@ @\n@@@')
    elif digit == 4:
        print('  @\n@ @\n@ @\n@@@\n @ \n @ ')
    elif digit == 3:
        print('@@@\n  @\n@@ \n  @\n  @\n@@@')
    elif digit == 2:
        print('@@@\n  @\n @ \n@  \n@  \n@@@')
    elif digit == 1:
        print(' @ \n@@ \n @ \n @ \n @ \n @ ')


main()