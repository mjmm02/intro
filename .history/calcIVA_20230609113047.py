def main():

    prod = float(input("Introduze o produto: ")
    cIVA(prod)
    print(prod)

def cIVA(p):
    p += p*.23
    return(p)

main()