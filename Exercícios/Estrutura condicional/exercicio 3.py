while True:
    ano_atual = int(input("Digite o ano atual: "))
    if ano_atual >= 100:
        break
    else:
        print("valor inválido.")
while True:
    data_nascimento = int(input("Digite o data de nascimento: "))
    if data_nascimento < ano_atual and data_nascimento > 0:
        break
    else:
        print("valor inválido.")

idade = ano_atual - data_nascimento
if idade >= 18:
    resultado = "maior"
else:
    resultado = "menor"
print(f"Você tem {idade} anos e é {resultado} de idade.")
