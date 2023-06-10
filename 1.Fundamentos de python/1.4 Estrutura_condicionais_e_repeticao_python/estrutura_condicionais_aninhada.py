conta_normal = False
conta_universitario = False

saldo = 2000.00
saque = 2500
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print("Saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com", saldo - saque, "utilizado do cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitario:
    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiente")
else:
    print("Conta invalida")