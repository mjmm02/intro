def main():

    prod = input("Introduze o produto: ")
    cIVA()
    print(prod)

def cIVA(p):
    return(p =+ p*.23)

main()