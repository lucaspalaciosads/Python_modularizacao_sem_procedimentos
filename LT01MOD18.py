#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
A = 0
B = 0

def Diferenca():
    global A, B
    if (A > B):
        Diferenca = A - B
    else:
        Diferenca = B - A
    print("A diferença é: ", Diferenca)
    
def main ():
    global A, B
    A = int(input("Digite o primeiro número: "))
    B = int(input("Digite o segundo número: "))
    Diferenca()

if __name__ == '__main__':
    main()