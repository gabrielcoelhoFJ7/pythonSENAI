import random

# Define loop como 1 para iniciar o jogo
loop = 1

# Enquanto loop for igual a 1, o jogo continua
while loop == 1:

    # Define ganhou como 0, indicando que o jogador ainda não ganhou
    ganhou = 0

    # Gera um número secreto aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)

    # Exibe uma mensagem de boas-vindas ao jogador
    print("\nBem vindo ao jogo de adivinha")

    # Loop para obter a dificuldade escolhida pelo jogador
    while True:
        try:
            # Solicita ao jogador que escolha uma dificuldade
            escolha = input("\nQual dificuldade (Difícil, Normal ou Fácil) você deseja seguir? ")

            # Verifica a escolha do jogador e define o número de vidas de acordo com a dificuldade
            if escolha == "Difícil" or escolha == "Dificil" or escolha == "dificil" or escolha == "difícil":
                vidas = 5
                break
            elif escolha == "Normal" or escolha == "normal":
                vidas = 10
                break
            elif escolha == "Fácil" or escolha == "Facil" or escolha == "fácil" or escolha == "facil":
                vidas = 15
                break
            else:
                print("\nescreva corretamente.\n")

        # Trata erros de valor, como entrada inválida
        except ValueError:
            print("\nErro tente novamente")

    # Exibe o número de vidas do jogador
    print(f"\nVocê tem {vidas} tentativas.")

    # Loop para o jogo principal
    while vidas != 0:

        # Loop para obter o número solicitado pelo jogador
        while True:
            try:
                # Solicita ao jogador que adivinhe um número
                numero_solicitado = int(input("Ok, agora tente adivinhar um número de 0 a 100: "))

                # Verifica se o número solicitado está dentro do intervalo válido
                if numero_solicitado >= 0 and numero_solicitado <= 100:
                    break
                else:
                    print("\nescreva corretamente.\n")
            # Trata erros de valor, como entrada inválida
            except ValueError:
                print("\nErro! Tente novamente!")

        # Verifica se o número solicitado é maior que o número secreto
        if numero_solicitado > numero_secreto:
            print("\nÉ menor que isso.")
            vidas -= 1
            print(f"\nVocê tem {vidas} tentativas.")

        # Verifica se o número solicitado é menor que o número secreto
        elif numero_solicitado < numero_secreto:
            print("\nÉ maior que isso.")
            vidas -= 1
            print(f"\nVocê tem {vidas} tentativas.")

        # Verifica se o número solicitado é igual ao número secreto
        else:
            vidas = 0
            ganhou = 1

    # Verifica se o jogador ganhou
    if ganhou == 1:
        print("\nBoa, você ganhou!")
    else:
        print(f"\nEita, você perdeu!\n o numero era {numero_secreto}")


    # Loop para perguntar ao jogador se deseja jogar novamente
    while True:
        try:
            # Solicita ao jogador que responda se deseja jogar novamente
            loop = input("\nDeseja jogar novamente? ")

            # Verifica a resposta do jogador e define loop de acordo
            if loop == "Não" or loop == "nao" or loop == "n" or loop == "não" or loop == "Nao":
                loop = 0
                print("Obrigado por jogar!")
                break
            elif loop == "Sim" or loop == "sim" or loop == "s" or loop == "ss":
                loop = 1
                break
            else:
                print("\nescreva corretamente.\n")
        # Trata erros de valor, como entrada inválida
        except ValueError:
            print("\nErro tente novamente")