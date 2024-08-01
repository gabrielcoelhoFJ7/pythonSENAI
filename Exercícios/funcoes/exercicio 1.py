from datetime import datetime

horario = datetime.now().hour
def saudacao(horario):
    if horario > 0 and horario <= 5:
        mensagem = "boa madrugada"
    elif horario > 5 and horario <= 12:
        mensagem = "bom dia"
    elif horario > 12 and horario <= 19:
        mensagem = "boa tarde"
    else:
        mensagem = "boa noite"
    return mensagem

def solicita_nome():
    while True:
        try:
            nome = input("Digite seu nome: ")

            return nome
        except ValueError:
            print("Erro, tente novamente")


def ola_nome(nome,horario):
    print("Olá", nome, saudacao(horario))

nome = solicita_nome()

ola_nome(nome,horario)
