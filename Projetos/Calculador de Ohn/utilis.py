def solicita_resistencia():
    while True:
        try:
            R = float(input("\nInsira a resistencia em Ω: "))
            if R > 0:
                return R
        except ValueError:
            print("Erro! Tente novamente.")

def solicita_tensao():
    while True:
        try:
            V = float(input("\nInsira a tensão em V: "))
            if V > 0:
                return V
        except ValueError:
            print("Erro! Tente novamente.")

def solicita_corrente():
    while True:
        try:
            I = float(input("\nInsira a corrente em A: "))
            if I > 0:
                return I
        except ValueError:
            print("Erro! Tente novamente.")

def solicita_TF():
    while True:
        try:
            TF = float(input("\nInsira a tensão da fonte em V: "))
            if TF > 0:
                return TF
        except ValueError:
            print("Erro! Tente novamente.")

def resistencia(V,I):
    R = V / I
    mensagem = "resistencia"
    return R

def tensao(R,I):
    V = R * I
    mensagem = "tensão"
    return V

def corrente(V,R):
    I = V / R
    mensagem = "corrente"
    return I

def resistencia_resistor(TF,V,I):
    R = ((TF - V) / I)
    mensagem = "resistencia"
    return R

def menu():
    escolha = int(input("\nOlá este programa calcula resistencia, corrente, tensão e resistencia do resistor."
                        "\n\n[1] resistencia\n[2] corrente\n[3] tensão\n[4] resistencia do resistor\n\n"
                        "Atenção! Caso o número desejado for decimal coloque ponto em vez de virgula.\n\n"
                        "Digite um numero para escolher: "))
    V = 0.0
    I = 0.0
    R = 0.0
    TF = 0.0
    return escolha

def exibir(nomenclatura,valor):
    print(f"Sua {nomenclatura} é {valor}Ω.")

def repeticao_():
    while True:
        try:
            repeticao = int(input("Deseja repetir?\n[1]Sim\n[0]Não\n>> "))
            if repeticao == 1 or repeticao == 0:
                return repeticao
        except ValueError:
            print("Erro, tente novamente")
