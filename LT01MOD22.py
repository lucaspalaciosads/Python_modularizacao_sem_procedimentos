#22.	Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
N1 = 0
N2 = 0

def crescente():
    global N1, N2
    if N1 > N2:
        print(N2,", ", N1)
    else:
        print(N1,", ", N2)

def main():
    global N1, N2
    N1 = int(input("Digite o primeiro número: "))
    N2 = int(input("Digite o segundo número: "))
    crescente()

if __name__ == "__main__":
    main()
