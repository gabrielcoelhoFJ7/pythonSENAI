def solicita_num2():
    num1 = float(input("insira o primeiro número: "))
    return num1

def solicita_num1():
    num2 = float(input("insira o segundo número: "))
    return num2

def escolha_menu():
    print("Menu calculadora\n1 - Soma\n2 - subtração\n3 - Multiplicação\n4 - divisão")
    escolha = input("Insira a sua escolha: ")
    return escolha

def menu(escolha):
    if escolha == "1":
        exibir(soma(solicita_num1(),solicita_num2()))
    elif escolha == "2":
        exibir(subtracao(solicita_num1(),solicita_num2()))
    elif escolha == "3":
        exibir(multiplicacao(solicita_num1(),solicita_num2()))
    elif escolha == "4":
        exibir(divisao(solicita_num1(),solicita_num2()))




# adição
def soma(num1, num2):
    resultado = num1 + num2
    return resultado


# subtração
def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado


# multiplicação
def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado

# divisão
def divisao(num1, num2):
    resultado = num1 / num2
    return resultado


def exibir(resultado):
    print(f"O resultado é {resultado}")

repeticao = True
while repeticao:
    menu(escolha_menu())
    repeticao = input("deseja continuar? [S/N] ")
    if repeticao == "S":
        repeticao = True
    elif repeticao == "N":
        repeticao = False
        print("Obrigado por usar o programa!")
    else:
        print("Erro, tente novamente.")

