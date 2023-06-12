def main():

    prod = cIVA(int(input("Introduze o preço do produto: ")))
#   prod = cIVA(prod)
    print('Preço com IVA: ', prod)

def cIVA(p):
    p += p * 0.23
    return (p)

main()