def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Exibir números de 1 a 10")
        print("2. Exibir números pares")
        print("3. Exibir tabuada")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            for numero in range(1, 11):
                print(numero)

        elif opcao == 2:
            for numero in range(2, 11, 2):
                print(numero)

        elif opcao == 3:
            numero = int(input("Digite um número: "))

            for valor in range(1, 11):
                print(f"{numero} x {valor} = {numero * valor}")

        elif opcao == 4:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

menu()
