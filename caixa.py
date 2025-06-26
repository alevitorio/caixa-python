# Dados do usuario [nome, conta, senha, saldo]
usuario = ["Alessandro", "12345-6", "123", 1000.49]

print("="*40)
print(" BEM-VINDO AO CAIXA ELETRONICO ")
print("="*40)

# Tela de login
logado = False
while not logado:
    conta_input = input("Digite sua conta: ")
    senha_input = input("Digite sua senha: ")

    if conta_input == usuario[1] and senha_input == usuario[2]:
        print(f"\n Ola, {usuario[0]}! Bem-vindo ao caixa eletronico.\n")
        logado = True
    else:
        print(" Conta ou senha invalida. Tente novamente.\n")

# Menu de opcoes
while True:
    print("\nSelecione uma opcao:")
    print("1 - Consultar saldo")
    print("2 - Realizar saque")
    print("3 - Sair")

    opcao = input("Digite sua opcao: ")

    if opcao == "1":
        print(f"\n Seu saldo atual e: R${usuario[3]:.2f}")

    elif opcao == "2":
        limite = 1500
        print("\n Informe o valor do saque (multiplo de 10)")
        valor = int(input("Valor: "))

        if valor > limite:
            print(" Limite maximo por saque e de R$1500,00.")
        elif valor > usuario[3]:
            print(" Saldo insuficiente.")
        elif valor % 10 != 0:
            print(" O valor deve ser multiplo de R$10,00.")
        else:
            # Calcular notas
            nota100 = nota50 = nota20 = nota10 = 0
            resto = valor

            while resto > 0:
                if resto >= 100:
                    nota100 += 1
                    resto -= 100
                elif resto >= 50:
                    nota50 += 1
                    resto -= 50
                elif resto >= 20:
                    nota20 += 1
                    resto -= 20
                elif resto >= 10:
                    nota10 += 1
                    resto -= 10

            usuario[3] -= valor

            print("\n Saque realizado com sucesso!")
            print(f" Notas entregues:")
            if nota100 > 0:
                print(f" - {nota100} nota(s) de R$100,00")
            if nota50 > 0:
                print(f" - {nota50} nota(s) de R$50,00")
            if nota20 > 0:
                print(f" - {nota20} nota(s) de R$20,00")
            if nota10 > 0:
                print(f" - {nota10} nota(s) de R$10,00")
            print(f"\n Saldo atual: R${usuario[3]:.2f}")

    elif opcao == "3":
        print(f"\n Obrigado, {usuario[0]}! Volte sempre.")
        break

    else:
        print(" Opcao invalida. Tente novamente.")
