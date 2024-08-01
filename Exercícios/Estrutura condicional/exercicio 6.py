
while True:
    num_1 = int(input("digite um numero"))
    num_2 = int(input("digite outro numero"))
    num_3 = int(input("digite outro numero"))
    if num_1 > num_2 and num_1 > num_3:
        print(f"O número {num_1} é o maior.")
        break
    elif num_2 > num_1 and num_2 > num_3:
        print(f"O número {num_2} é o maior.")
        break
    elif num_3 > num_1 and num_3 > num_2:
        print(f"O número {num_3} é o maior.")
        break
    else:
        print("Erro, tente novamente!")
