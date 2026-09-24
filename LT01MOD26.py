#26.	Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
N1 = 0
N2 = 0

def verificar_multiplo():
    global N1, N2
    if N1 < N2:
        if N2 % N1 == 0:
            print("O número {} é múltiplo de {}".format(N2, N1))
        else:
            print("O número {} não é múltiplo de {}".format(N2, N1))
    elif N1 > N2:
        if N1 % N2 == 0:
            print("O número {} é múltiplo de {}".format(N1, N2))
        else:
            print("O número {} não é múltiplo de {}".format(N1, N2))
    else:
        print("Os números são iguais e, portanto, múltiplos entre si.")
        
def main():
    global N1, N2
    N1 = int(input("Digite o primeiro valor: "))
    N2 = int(input("Digite o segundo valor: "))
    verificar_multiplo()

if __name__ == "__main__":
    main()