#24.	Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
V1 = 0

def verificar_divisibilidade():
    global V1
    if V1 % 2 == 0 and V1 % 3 == 0:
        print("O número é divisível por 2 e 3.")
    elif V1 % 2 == 0 and V1 % 3 != 0:
        print("O número é divisível por 2 mas não por 3.")
    elif V1 % 2 != 0 and V1 % 3 == 0:
        print("O número é divisível por 3 mas não por 2.")
    else:
        print("O número não é divisível por 2 e 3.")

def main():
    global V1
    V1 = int(input("Digite um número: "))
    verificar_divisibilidade()

if __name__ == "__main__":
    main()