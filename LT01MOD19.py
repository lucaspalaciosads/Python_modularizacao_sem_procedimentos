#19.Receba 2 valores reais. Calcule e mostre o maior deles.
N1 = 0.0
N2 = 0.0

def maior():
    global N1, N2
    if N1 > N2:
        print("O maior valor é: ", N1)
    elif N2 > N1:
        print("O maior valor é: ", N2)
    else:
        print("Os valores são iguais.")
        
def main():
    global N1, N2
    N1 = float(input("Digite o primeiro valor: "))
    N2 = float(input("Digite o segundo valor: "))
    maior()

if __name__ == "__main__":
    main()