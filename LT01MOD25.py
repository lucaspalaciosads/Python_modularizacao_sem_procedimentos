#25.Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
HI = 0
HF = 0
MI = 0
MF = 0

def calcular_tempo_jogo():
    global HI, HF, MI, MF
    T = (HF * 60 + MF) - (HI * 60 + MI)
    if T < 0:
        T = T + 1440
    H = T // 60
    M = T % 60
    print("O tempo total é de", H, "hora(s) e", M, "minuto(s)")

def main():
    global HI, HF, MI, MF
    HI = int(input("Digite a hora de início: "))
    MI = int(input("Digite o minuto de início: "))
    HF = int(input("Digite a hora de final: "))
    MF = int(input("Digite o minuto de final: "))
    calcular_tempo_jogo()

if __name__ == "__main__":
    main()