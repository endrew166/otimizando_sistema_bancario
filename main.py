def cliente_cadastro(cliente):
    # Solicita o CPF do cliente
    cpf = input("Digite o CPF: ")

    # Verifica se o CPF já está cadastrado
    confirma = cpf in cliente
    if not confirma:
        # Solicita os dados do cliente caso o CPF não esteja cadastrado
        nome = input("Digite o Nome: ")
        data_nascimento = input("Digite a Data de Nascimento: ")
        logradouro = input("Digite o Logradouro: ")
        numero = input("Digite o Número: ")
        bairro = input("Digite o Bairro: ")
        cidade = input("Digite a Cidade: ")
        sigla_estado = input("Digite a Sigla do Estado: ")

        # Formata o endereço do cliente
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade} / {sigla_estado}"

        # Atualiza o dicionário de clientes com os novos dados
        cliente.update({
            cpf: {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco
            }
        })
    else:
        # Mensagem de cliente já cadastrado
        print("Cliente já cadastrado.")


def cadastro_conta(contas, numero_conta):
    # Solicita o CPF do cliente para vincular à conta
    cpf_conta = input("Digite o CPF: ")

    # Verifica se o CPF está cadastrado no sistema de clientes
    if cpf_conta in cliente.keys():
        # Verifica se o CPF não possui contas associadas e cria uma lista de contas
        if cpf_conta not in contas:
            contas[cpf_conta] = []

        # Cria um novo dicionário para a conta
        nova_conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "cpf": cpf_conta
        }

        # Adiciona a nova conta à lista de contas do cliente
        contas[cpf_conta].append(nova_conta)

        # Incrementa o número da conta para o próximo cadastro
        numero_conta += 1

        # Exibe as informações da conta adicionada
        print("Conta adicionada:")
        if cpf_conta in cliente.keys():
            print(cliente[cpf_conta])
        for conta in contas[cpf_conta]:
            print(conta)
    else:
        # Mensagem de erro se o CPF não estiver cadastrado
        print("CPF não está cadastrado.")


def depositar(valor, saldo, extrato):
    # Adiciona o valor depositado ao saldo
    saldo += valor
    # Adiciona o saldo atualizado ao extrato
    extrato.append(saldo)
    # Confirma o depósito realizado
    print("Depósito realizado com sucesso.")

    return saldo, extrato


def saque(*, valor_saque, saldo, extrato02):
    # Subtrai o valor do saque do saldo
    saldo -= valor_saque
    # Adiciona o valor do saque ao extrato
    extrato02.append(valor_saque)
    # Confirma o saque realizado
    print("Saque feito com sucesso.")

    return saldo, extrato02


def extrato_func(saldo, /, extrato, extrato02):
    # Verifica se há transações de depósito para exibir
    if extrato:
        for i in extrato:
            if i > 0:
                print(f"Valor depositado: R$ {i:.2f}")

    # Verifica se há transações de saque para exibir
    if extrato02:
        for i in extrato02:
            if i > 0:
                print(f"Valor retirado: R$ {i:.2f}")

    # Mensagem caso não haja transações
    if not extrato and not extrato02:
        print("Nenhuma transação registrada.")

    # Exibe o saldo final
    print(f"Saldo final: R$ {saldo:.2f}")


# Texto do menu principal
texto = """ 
    Menu do Banco
    [1] - Cadastrar Cliente:
    [2] - Cadastrar Conta Corrente:
    [3] - Depositar:
    [4] - Sacar:
    [5] - Verificar Extrato:
    [0] - Sair:
"""

# Inicialização de variáveis
saldo = 0
extrato = []
extrato02 = []
valor_saque = 0
cliente = {}
agencia = "0001"
numero_conta = 1
contas = {}

# Loop principal do sistema
while True:
    # Exibe o menu e solicita a opção do usuário
    opcao = input(texto)

    if opcao == "1":
        # Chama a função para cadastro de clientes
        cliente_cadastro(cliente)

    elif opcao == "2":
        # Chama a função para cadastro de contas
        cadastro_conta(contas, numero_conta)

    elif opcao == "3":
        # Solicita o valor do depósito
        valor = float(input("Valor a ser depositado: R$ "))

        # Verifica se o valor é maior que zero
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
        else:
            # Realiza o depósito e atualiza o saldo e o extrato
            saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "4":
        print("Saque")
        # Solicita o valor do saque
        valor_saque = float(input("Valor que deseja sacar: R$ "))

        # Verifica os critérios para saque: limite de valor, saldo suficiente e limite de saques diários
        if valor_saque <= 500 and saldo >= valor_saque and len(extrato02) < 3:
            # Realiza o saque e atualiza o saldo e o extrato
            saldo, extrato02 = saque(valor_saque=valor_saque, saldo=saldo, extrato02=extrato02)
        else:
            # Mensagens de erro para cada critério não atendido
            if valor_saque > 500:
                print("O valor máximo para saque é R$ 500.")
            if saldo < valor_saque:
                print("Saldo insuficiente.")
            if len(extrato02) >= 3:
                print("Limite de saques diários atingido.")

    elif opcao == "5":
        # Chama a função para exibir o extrato
        print("Extrato:")
        extrato_func(saldo, extrato=extrato, extrato02=extrato02)

    elif opcao == "0":
        # Encerra o loop e sai do programa
        break

    else:
        # Mensagem para opção inválida
        print("Operação inválida, por favor selecione novamente a operação desejada.")
