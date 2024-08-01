repeticao = 0
while repeticao != 1:
    escolha = int(input("\nOlá este programa calcula resistencia, corrente, tensão e resistencia do resistor.\n\n[1] resistencia\n[2] corrente\n[3] tensão\n[4] resistencia do resistor\n\nAtenção! Caso o número desejado for decimal coloque ponto em vez de virgula.\n\nDigite um numero para escolher: "))
    V = 0.0
    I = 0.0
    R = 0.0
    TF = 0.0
    if escolha == 1:
        while True:
            try:
                V = float(input("\nInsira a tensão em V: "))
                if V > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")
        while True:
            try:
                I = float(input("Insira a corrente em A: "))
                if I > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")



        if V <= 0 or I <= 0:
            mensagem = "\nerro, tente novamente."
            print(mensagem)
            repeticao = 0
        else:
            R = V / I
            mensagem = f"Sua resistencia é {R}Ω."
            repeticao = 1

    elif escolha == 2:
        while True:
            try:
                V = float(input("\nInsira a tensão em V: "))
                if V > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")

        while True:
            try:
                R = float(input("Insira a resistencia em Ω: "))
                if R > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")

        if V <= 0 or R <= 0:
            mensagem = "\nerro, tente novamente."
            print(mensagem)
            repeticao = 0
        else:
            I = V / R
            mensagem = f"Sua corrente é {I}Ω."
            repeticao = 1
    elif escolha == 3:
        while True:
            try:
                R = float(input("\nInsira a resistencia em Ω: "))
                if R > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")
        while True:
            try:
                I = float(input("Insira a corrente em A: "))
                if I > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")

        if I <= 0 or R <= 0:
            mensagem = "\nerro, tente novamente."
            print(mensagem)
            repeticao = 0
        else:
            V = R * I
            mensagem = f"Sua tensão é {V}Ω."
            repeticao = 1
    elif escolha == 4:
        while True:
            try:
                TF = float(input("\nInsira a tensão da fonte em V: "))
                if TF > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")
        while True:
            try:
                V = float(input("Insira a tensão em V: "))
                if V > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")
        while True:
            try:
                I = float(input("Insira a corrente em A: \n"))
                if I > 0:
                    break
            except ValueError:
                print("Erro! Tente novamente.")

        if V <= 0 or I <= 0:
            mensagem = "erro, tente novamente."
            print(mensagem)
            repeticao = 0
        else:
            R = ((TF - V) / I)
            mensagem = f"Sua resistencia é {R}Ω."
            repeticao = 1
    else:
        print("\nerro, tente novamente\n")
        repeticao = 0
#print(f"\n{mensagem}")
input("\nprecione enter para sair ")

    # Tensão Elétrica: V = R.I
    #Corrente Elétrica: I = V ÷ R
    #Resistência Elétrica: R = V ÷ I
