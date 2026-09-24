#20.Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
A = 0
B = 0
C = 0

def calcular_raizes():
    global A, B, C
    if A <= 0:
        print("O valor de A deve ser maior que zero.")
    else:
        Delta = (B ** 2) - (4 * A * C)
        print("O valor de Delta é:", Delta)
        if Delta < 0:
            print("Não existem raízes reais.")
        elif Delta == 0:
            X1 = -B / (2 * A)
            print("A equação possui uma raiz real: X =", X1)
        else:
            X1 = (-B + (Delta ** 0.5)) / (2 * A)
            X2 = (-B - (Delta ** 0.5)) / (2 * A)
            print(f"A equação possui duas raízes reais: X1 = {X1:.2f} e X2 = {X2:.2f}")
    
def main():
    global A, B, C
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    calcular_raizes()
    
if __name__ == "__main__":
    main()