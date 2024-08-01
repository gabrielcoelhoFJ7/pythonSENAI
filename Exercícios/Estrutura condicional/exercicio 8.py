
while True:
    renda = float(input("Digite o valor da sua renda bruta: "))
    if renda <= 56072 and renda > 0:
        aliquota = 0
        break
    elif renda > 56072 and renda <= 238532:
        aliquota = 7.5
        break
    elif renda > 238532 and renda <= 522400:
        aliquota = 15
        break
    elif renda > 522400 and renda <= 987600:
        aliquota = 22.5
        break
    elif renda > 987600:
        aliquota = 27.5
        break
    else:
        print("Erro, tente novamente")

imposto = renda * aliquota
imposto = imposto / 100

print(f"A aliquota é {aliquota}%\nO imposto de renda é R${imposto}.")


