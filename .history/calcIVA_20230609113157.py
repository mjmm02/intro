def main():

    prod = int(input("Introduze o produto: "))
    cIVA(prod)
    print(prod)

def cIVA(p):
    p * 0.23
    return(p)

main()