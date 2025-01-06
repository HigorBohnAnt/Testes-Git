def calculadora():
    print("Bem-vindo à Calculadora em Python!")
    print("Selecione a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    while True:
        # Entrada do usuário para a operação
        escolha = input("Escolha uma opção (1/2/3/4): ")

        # Verifica se a entrada é válida
        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue

            if escolha == '1':
                print(f"O resultado de {num1} + {num2} é {num1 + num2}")
            elif escolha == '2':
                print(f"O resultado de {num1} - {num2} é {num1 - num2}")
            elif escolha == '3':
                print(f"O resultado de {num1} * {num2} é {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"O resultado de {num1} / {num2} é {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")

        # Pergunta ao usuário se deseja continuar
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por usar a calculadora. Até a próxima!")
            break

# Executa a calculadora
calculadora()
