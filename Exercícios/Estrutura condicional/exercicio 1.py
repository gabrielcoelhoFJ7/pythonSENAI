print("Descubra se seu número é positivo ou negativo.")

resultado = ""

while True:
    try:
        num = float(input("Digite um valor: "))
        if num < 0:
            resultado = "negativo"
            break
        elif num > 0:
            resultado = "positivo"
            break
        elif num == 0:
            resultado = "neutro"
            break
        else:
            print("Erro de digitação.")
    except ValueError:
        print("Erro, tente novamente. Ex: 7.")
print(f"O valor digitado ({num}) é {resultado}.")