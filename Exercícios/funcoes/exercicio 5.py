def verifica(altura, peso):

  if altura != 0:
    imc = (peso / (altura * altura))
  else:
    imc = 0

  return imc

def verifica_imc(imc):
  if imc < 18.5:
    resultado = "abaixo do peso"
  elif imc >= 18.5 and imc < 25:
    resultado = "com o peso normal"
  elif imc >= 25 and imc < 30:
    resultado = "com sobrepeso"
  elif imc >= 30:
    resultado = "com obesidade"
  return resultado

#função
while True:
  altura = float(input("Digite sua altura em metros: "))
  peso = float(input("Digite seu peso em kilogramas: "))
  imc = verifica(altura, peso)
  if imc >= 0:
   break
  else:
    print("Erro, tente novamente.")

print(f"seu imc é {imc}.\nvocê está {verifica_imc(imc)}.")
