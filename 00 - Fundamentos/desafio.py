def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza uma operação de saque na conta.
    
    Argumentos:
        saldo (float): Saldo atual da conta
        valor (float): Valor a ser sacado
        extrato (str): Histórico de movimentações
        limite (float): Limite máximo por saque
        numero_saques (int): Número de saques já realizados
        limite_saques (int): Limite máximo de saques permitidos
    
    Retorno:
        tuple: Tupla contendo (saldo, extrato, numero_saques)
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Falha! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Falha! O valor do saque excede o limite do caixa.")
    elif excedeu_saques:
        print("Falha! Número máximo de saques por dia excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Falha! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato, /):
    """
    Realiza uma operação de depósito na conta.
    
    Argumentos:
        saldo (float): Saldo atual da conta
        valor (float): Valor a ser depositado
        extrato (str): Histórico de movimentações
    
    Retorno:
        tuple: Tupla contendo (saldo, extrato)
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Falha! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato bancário da conta.
    
    Argumentos:
        saldo (float): Saldo atual da conta
        extrato (str): Histórico de movimentações
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Cria um novo usuário no sistema.
    
    Argumentos:
        usuarios (list): Lista de usuários existentes
    
    Retorno:
        list: Lista atualizada de usuários
    """
    cpf = input("Informe o CPF (somente números): ")
    
    usuario_existente = filtrar_usuario(cpf, usuarios)
    if usuario_existente:
        print("Já existe usuário com esse CPF!")
        return usuarios
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return usuarios


def filtrar_usuario(cpf, usuarios):
    """
    Filtra usuários por CPF.
    
    Argumentos:
        cpf (str): CPF a ser pesquisado
        usuarios (list): Lista de usuários
    
    Retorno:
        dict or None: Usuário encontrado ou None
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    """
    Cria uma nova conta corrente.
    
    Argumentos:
        agencia (str): Número da agência
        numero_conta (int): Número da conta
        usuarios (list): Lista de usuários
        contas (list): Lista de contas existentes
    
    Retorno:
        tuple: Tupla contendo (contas, numero_conta)
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print("Usuário não encontrado! Fluxo de criação de conta encerrado.")
        return contas, numero_conta
    
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    
    contas.append(nova_conta)
    print("Conta criada com sucesso!")
    return contas, numero_conta + 1


def listar_contas(contas):
    """
    Lista todas as contas correntes.
    
    Argumentos:
        contas (list): Lista de contas
    """
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    print("\n=============== CONTAS ===============")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)
    print("======================================")


def main():
    """
    Função principal do sistema bancário.
    """

    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    numero_conta = 1
    
    while True:
        print("\n=============== MENU ===============")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Novo Usuário")
        print("[5] Nova Conta")
        print("[6] Listar Contas")
        print("[0] Sair")
        print("===================================")
        
        opcao = input("Selecione uma opção: ")
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            usuarios = criar_usuario(usuarios)
            
        elif opcao == "5":
            contas, numero_conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios, contas)
            
        elif opcao == "6":
            listar_contas(contas)
            
        elif opcao == "0":
            print("Obrigado por utilizar nosso sistema!")
            break
            
        else:
            print("Operação inválida! Selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()