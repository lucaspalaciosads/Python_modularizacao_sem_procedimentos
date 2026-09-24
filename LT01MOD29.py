#29.	Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
Tipo_investimento = 0
Valor_investimento = 0.0

def calcular_valor_corrigido(Tinv, Vinv):
    if Tinv == 1:
        Result = Vinv * 1.03
        print("O valor corrigido em 30 dias: R$ ", Result)
    elif Tinv == 2:
        Result = Vinv * 1.05
        print("O valor corrigido em 30 dias: R$ ", Result)
    else:
        print("Tipo de investimento inválido.")

def main():
    global Tipo_investimento, Valor_investimento
    Valor_investimento = float(input("Digite o valor do investimento: R$ "))
    Tipo_investimento = int(input("Digite o tipo de investimento (1 - poupança, 2 - renda fixa): "))
    calcular_valor_corrigido(Tipo_investimento, Valor_investimento)

if __name__ == "__main__":
    main()