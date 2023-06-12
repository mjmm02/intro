def main():

    prod = input("Introduze o produto: ")
    cIVA()
    print(prod)

float cIVA(p):
    return(p += p*.23)

main()