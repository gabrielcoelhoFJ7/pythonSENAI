from datetime import datetime

def solicita_nome():
    nome = input('Qual o seu nome? ')
    return nome

def saudacao(hora_atual):
    if hora_atual >= 0 and hora_atual <= 5:
        saudacao = "boa madrugada "
    elif hora_atual <= 12:
        saudacao = "bom dia "
    elif hora_atual <= 19:
        saudacao = "boa tarde "
    else:
        saudacao = "boa noite "

    return saudacao

def exibir_mensagem(nome, saudacao):
    print(saudacao + nome)

exibir_mensagem(solicita_nome(), saudacao(datetime.now().hour))


