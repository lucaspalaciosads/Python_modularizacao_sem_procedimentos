#21.Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
N1 = 0.0
N2 = 0.0
N3 = 0.0
N4 = 0.0

def calcular_media():
    global N1, N2, N3, N4
    Media = (N1 + N2 + N3 + N4) / 4
    print("A média das notas é:", Media)
    if Media >= 6:
        print("O aluno foi aprovado.")
    elif Media >= 3:
        print("O aluno está em exame.")
    else:
        print("O aluno foi reprovado.")
        print(f"A média aritmética é: {Media:.2f}")

def main():
    global N1, N2, N3, N4

    N1 = float(input("Digite a primeira nota: "))
    N2 = float(input("Digite a segunda nota: "))
    N3 = float(input("Digite a terceira nota: "))
    N4 = float(input("Digite a quarta nota: "))

    calcular_media()

if __name__ == "__main__":
    main()