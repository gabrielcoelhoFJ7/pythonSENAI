# Importa o módulo random
import random

# Variável para controlar a repetição do jogo
repeticao = 1

# Loop principal do jogo
while repeticao == 1:
    # Exibe uma mensagem de boas-vindas
    print("Bem vindo ao jogo par ou impar")

    # Loop para validar a escolha do jogador
    while True:
        try:
            # Solicita a escolha do jogador
            escolha = str(input("Par ou Impar? "))

            # Verifica se a escolha é válida
            if escolha == "Par" or escolha == "par" or escolha == "Impar" or escolha == "impar":
                break
            else:
                print("\nescreva corretamente.\n")
        except ValueError:
            # Exibe uma mensagem de erro caso a escolha seja inválida
            print("Erro! Tente novamente.")

    # Define a escolha da máquina com base na escolha do jogador
    if escolha == "Impar" or escolha == "impar":
        escolha_da_maquina = 0
    elif escolha == "Par" or escolha == "par":
        escolha_da_maquina = 1

    # Loop para validar o número do jogador
    while True:
        try:
            # Solicita o número do jogador
            numero_do_jogador = float(input("Escolha um número de 1 a 10 para poder competir comigo: "))

            # Verifica se o número é válido
            if numero_do_jogador >= 0 and numero_do_jogador <= 10:
                break
            else:
                print("\nResposta inválida. Ex: 10\n")
        except ValueError:
            # Exibe uma mensagem de erro caso o número seja inválido
            print("Erro! Tente novamente.")

    # Gera um número aleatório para a máquina
    numero_da_maquina = random.randint(1, 10)

    # Calcula o resto da soma dos números
    resto = (numero_da_maquina + numero_do_jogador) % 2

    # Verifica se a soma é par ou ímpar
    if resto == 0:
        resultado_da_soma = 0
        print(f"Meu número é {numero_da_maquina}")
        print("A soma é par")
    else:
        resultado_da_soma = 1
        print(f"Meu número é {numero_da_maquina}")
        print("A soma é impar")

    # Verifica o resultado do jogo
    if resultado_da_soma == 0 and escolha_da_maquina == 0:
        print("Você perdeu!")
    elif resultado_da_soma == 0 and escolha_da_maquina == 1:
        print("Você ganhou!")
    elif resultado_da_soma == 1 and escolha_da_maquina == 0:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    # Verifica se o jogador deseja continuar jogando
    while True:
        try:
            # Solicita a confirmação do jogador
            repeticao = input("Quer continuar? [S/N] ")

            # Verifica se a confirmação é válida
            if repeticao == "S" or repeticao == "s":
                repeticao = 1
                break
            elif repeticao == "N" or repeticao == "n":
                repeticao = 0
                break
            else:
                print("\nescreva corretamente.\n")

        except ValueError:
            # Exibe uma mensagem de erro caso a confirmação seja inválida
            print("Erro! Tente novamente.")