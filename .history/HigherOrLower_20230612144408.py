import random
import os
# import sys


def main():



    n = random.randint(1, 10)
    x = 3
    while 1:
        num = input("Choose a number between 1 and 10: ")
        num = int(num)
        if num == n:
            print("A winner is you!")
            break
        elif x == 0:
            print("Game over!")
            break
        elif num < 1 or num > 10:
            print("You selected an invalid number!")
        elif num > n:
            print("Wrong! Choose a lower number!")
        elif num < n:
            print("Wrong! Choose a higher number!")
        y = str(x)
        print("You have " + y + " more tries!")
        x -= 1




main()