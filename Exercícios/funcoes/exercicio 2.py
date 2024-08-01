

def menu_temperatura():
    print("Menu temperatura")
    print("1 - Fahrenheit")
    print("2 - Kelvin")

def solicita_escolha():
    escolha = input("Escolha: ")
    return escolha

def soliita_celsius():
    while True:
        try:
            graus_celsius = float(input("Insira a temperatura em graus celsius: "))

            return graus_celsius
        except ValueError:
            print("Erro, tente novamente")


def escolha_menu(escolha, graus_celsius):
    if escolha == "1":
        temperatura = graus_celsius * 1.8 + 32
    else:
        temperatura = graus_celsius + 273.15

    return temperatura

def exibir():
    print("A temperatura é",escolha_menu(solicita_escolha(),soliita_celsius()))

menu_temperatura()
exibir()
