def calculadora():
    while True:
        print("\nEscolha a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            print("Bye bye!")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existente")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = num1 + num2
            print(f"O resultado de {num1} + {num2} é: {resultado}")

        elif opcao == '2':
            resultado = num1 - num2
            print(f"O resultado de {num1} - {num2} é: {resultado}")

        elif opcao == '3':
            resultado = num1 * num2
            print(f"O resultado de {num1} * {num2} é: {resultado}")

        elif opcao == '4':
            if num2 == 0:
                print("Erro a operação não é permitida.")
            else:
                resultado = num1 / num2
                print(f"O resultado de {num1} / {num2} é: {resultado}")

# função calculadora
calculadora()
