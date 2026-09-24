#28.	Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
preco_atual = 0.0
media_mensal = 0.0

def calcular_novo_preco(PA, VM):
    if VM < 500 and PA < 30:
        NV = PA * 1.10
        print("O novo preço do produto é: R$ ", NV)
    elif VM >= 500 and VM < 1000 and PA >= 30 and PA < 80:
        NV = PA * 1.15
        print("O novo preço do produto é: R$ ", NV)
    elif VM >= 1000 and PA >= 80:
        NV = PA * 0.95
        print("O novo preço do produto é: R$ ", NV)
    else:
        NV = PA
        print("O preço do produto permanecerá: R$ ", NV)
        
def main():
    global preco_atual, media_mensal
    preco_atual = float(input("Digite o preço atual do produto: R$ "))
    media_mensal = float(input("Digite a média mensal de vendas: "))
    calcular_novo_preco(preco_atual, media_mensal)

if __name__ == "__main__":
    main()