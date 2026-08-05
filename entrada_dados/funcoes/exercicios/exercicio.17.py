def trocar_valores():
    a = input("Digite o valor de A: ")
    b = input("Digite o valor de B: ")

    print(f"\nAntes:\nA = {a}\nB = {b}")

    a, b = b, a

    print(f"\nDepois:\nA = {a}\nB = {b}")

trocar_valores()