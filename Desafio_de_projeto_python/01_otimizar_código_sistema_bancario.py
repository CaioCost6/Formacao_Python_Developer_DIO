import textwrap

def menu(): 
    
    menu = """\n 

    ================ MENU ================== 

    [D]\tDepositar 
    [S]\tSacar 
    [E]\tExtrato 
    [NC]\tNova conta 
    [LC]\tListar contas 
    [NU]\tNovo usuário 
    [X]\tSair 
   
    => """ 
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /): 
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("Deposito realizado com sucesso") 
    else:
        print("Operação invalida")

    return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite, numero_saques): 
    saldo_total = saldo+limite

    if saldo_total < valor:
        print("Saldo insuficiente")

    elif numero_saques == 0: 
        print("Limite de saques diários atingido") 

    elif valor > 0: 
        saldo -= valor 
        extrato += f"Saque:\tR${valor:.2f}\n" 
        numero_saques -= 1
        print("Saque realizado com sucesso") 
    else: 
        print("Operação falhou, favor verificar as informações") 
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): 

    print("\n================EXTRATO=====================") 
    print("Não foram realizados transações." if not extrato else extrato) 
    print(f"\nSaldo:\tR${saldo:.2f}\n") 

    print("===============================================")       

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (só número): ") 
    usuario = filtrar_usuario(cpf, usuarios)   

    if usuario: 
        print("Já existe cadastro para esse usuário") 
        return 

    nome = input("Digite nome do usuário completo: ") 
    data_nascimento = input("Digite data de nascimento (dd-mm-aaaa): ") 
    endereco = input("Informe o endereço(logradouro, nro – bairro – cidade/sigla estado): ") 
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) 

    print("\n============Cadastro realizado com sucesso!=============") 

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def criar_conta(agencia, numero_conta, usuarios): 
    cpf = input("Informe o CPF (só número): ") 
    usuario = filtrar_usuario(cpf, usuarios)   

    if usuario: 
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!") 

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

def main(): 
    
    AGENCIA = "0001"
    saldo = 0 
    limite = 600
    extrato = "" 
    numero_saques = 3 
    usuarios = [] 
    contas = [] 

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor: ")) 
            saldo, extrato = deposito(saldo, valor, extrato) 

        elif opcao == "S":
            valor = float(input("Informe o valor: "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques,
                ) 

        elif opcao == "E": 
            exibir_extrato(saldo, extrato=extrato) 

        elif opcao == "NU": 
            criar_usuario(usuarios) 

        elif opcao == "NC": 
            numero_conta = len(contas) + 1 
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 

            if conta:
                contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)
        elif opcao == "X":
            break
        else:
            print("Operação invalida, favor verficar opção escolhida")
main()