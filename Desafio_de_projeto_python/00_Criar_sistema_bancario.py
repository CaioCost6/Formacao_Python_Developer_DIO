menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        deposito = float(input("Qual valor deseja depositar:"))
        if deposito > 0:
            print("Desposito concluído\nObrigado pela preferência")
            saldo = saldo + deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Valor invalido")

    elif opcao == "S":
        saque = float(input("Valor que deseja sacar:"))

        excedeu_saldo = saldo < saque

        excedeu_limite = saque > limite

        excedeu_saques = numero_saque > LIMITE_SAQUE

        if excedeu_saldo:
            print("Saldo insuficiente")
        
        elif excedeu_limite:
            print("Limite por saques excedido")

        elif excedeu_saques:
            print("Limite de saques diario atingido")

        elif saque > 0:
            print("Saque realizado")
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saque = numero_saque + 1

        else:
            print("Operação invalida!")

    elif opcao == "E":
        print("\n==================== EXTRATO ================================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("================================================================")

    elif opcao == "X":
        print("Sair")
        break
    else:
        print("Operação invalida")