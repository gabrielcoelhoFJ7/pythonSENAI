from utilis import *

repeticao = 1

while repeticao != 0:

    escolha = menu()

    if escolha == 1:
        exibir("reistencia",resistencia(solicita_tensao(),solicita_corrente()))
        repeticao = repeticao_()
    elif escolha == 2:
        exibir("corrente",corrente(solicita_tensao(),solicita_resistencia()))
        repeticao = repeticao_()
    elif escolha == 3:
        exibir("tensão",tensao(solicita_resistencia(),solicita_corrente()))
        repeticao = repeticao_()
    elif escolha == 4:
        exibir("resistencia",resistencia_resistor(solicita_TF(),solicita_tensao(),solicita_corrente()))
        repeticao = repeticao_()
    else:
        print("Erro, tente novamente")
        repeticao = 1

input("\nprecione enter para sair ")

