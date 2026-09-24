#27.	Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.
voltas = 0
extensao_circuito = 0
tempo_duracao = 0

def calcular_velocidade_media(NV, EC, TD):
    DS = NV * EC / 1000
    DT = TD / 60
    Cont = DS / DT
    print("A velocidade média do carro é de: ", Cont, "Km/h")

def main():
    global voltas, extensao_circuito, tempo_duracao
    voltas = int(input("Digite o número de voltas: "))
    extensao_circuito = int(input("Digite a extensão do circuito (em metros): "))
    tempo_duracao = int(input("Digite o tempo de duração (em minutos): "))
    calcular_velocidade_media(voltas, extensao_circuito, tempo_duracao)

if __name__ == "__main__":
    main()