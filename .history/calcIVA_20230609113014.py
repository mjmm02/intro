def main():

    prod = input("Introduze o produto: ")
    cIVA()
    print(prod)

def cIVA(p):
    p += p*.23
    return(p)

main()