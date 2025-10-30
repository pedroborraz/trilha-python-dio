def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("O valor do saque é maior que o limite do caixa.")
    elif excedeu_saques:
        print("Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("O valor informado é inválido.")
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de: R$ {valor:.2f}\n"
    else:
        print("Valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return extrato, saldo

def menu():
    menu = """\n
    --------- MENU ---------

[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair

=> """
    return input(menu)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
