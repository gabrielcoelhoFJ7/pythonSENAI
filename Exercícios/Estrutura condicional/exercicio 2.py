media = ""
num_1 = 0
num_2 = 0
resultado = ""

num1 = int(input("insira a primeira nota: "))
num2 = int(input("insira a segunda nota: "))

media = (num_1 + num_2) / 2

while True:
    try:
        if media >= 70:
            resultado = "Aprovado"
            break
        elif media < 70:
            resultado = "Reprovado"
            break
        else:
            print("resposta inválida.")
    except ValueError:
        print("Erro, digite corretamente. Ex: 70.")
print(f"O aluno está {resultado}.")