
lado1 = float(input("Digite o tamanho em centímetros do primeiro lado do triangulo: "))

lado2 = float(input("Digite o tamanho em centímetros do segundo lado do triangulo: "))

lado3 = float(input("Digite o tamanho em centímetros do terceiro lado do triangulo: "))


def triangulo(lado1_, lado2_, lado3_):
    if lado1_ == lado2_ and lado1_ != lado3_ or lado1_ == lado3_ and not lado1_ == lado2_:
      triangulo = "isóceles"
    elif lado1_ == lado2_ and lado1_ == lado3_:
      triangulo = "equilátero"
    else:
      triangulo = "escaleno"
    return triangulo


def exibir(triangulo):
    print(f"o triangulo é {triangulo}.")


exibir(triangulo(lado1, lado2, lado3))