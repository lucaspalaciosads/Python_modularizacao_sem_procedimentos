#23.Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
V1 = 0
V2 = 0
V3 = 0
V4 = 0

def ordenar_4_numeros():
    global V1, V2, V3, V4
    if V4 <= V1:
        print(V4, ", ", V1, ", ", V2, ", ", V3)
    elif V4 > V1 and V4 <= V2:
        print(V1, ", ", V4, ", ", V2, ", ", V3)
    elif V4 > V2 and V4 <= V3:
        print(V1, ", ", V2, ", ", V4, ", ", V3)
    else:
        print(V1, ", ", V2, ", ", V3, ", ", V4)

def main():
    global V1, V2, V3, V4
    V1 = int(input("Digite o primeiro valor: "))
    V2 = int(input("Digite o segundo valor: "))
    V3 = int(input("Digite o terceiro valor: "))
    V4 = int(input("Digite o quarto valor: "))
    ordenar_4_numeros()

if __name__ == "__main__":
    main()